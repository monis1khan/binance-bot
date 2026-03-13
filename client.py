from binance.client import Client
from binance.exceptions import BinanceAPIException
import time

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret, logger):
        self.logger = logger

        # ✅ Enable testnet
        self.client = Client(api_key, api_secret, testnet=True)

        # ✅ Sync time with Binance
        self._sync_time()

    def _sync_time(self):
        try:
            server_time = self.client.get_server_time()
            server_timestamp = server_time["serverTime"]
            local_timestamp = int(time.time() * 1000)

            self.client.timestamp_offset = server_timestamp - local_timestamp
            self.logger.info(
                f"Time synced. Offset: {self.client.timestamp_offset} ms"
            )
        except Exception as e:
            self.logger.error("Failed to sync time", exc_info=True)
            raise

    def place_order(self, **kwargs):
        try:
            self.logger.info(f"Order request: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            self.logger.info(f"Order response: {response}")
            return response
        except BinanceAPIException as e:
            self.logger.error(f"Binance API error: {e}", exc_info=True)
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}", exc_info=True)
            raise