import argparse
import os
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import create_order
from bot.logging_config import setup_logger

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    logger = setup_logger()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API key or secret missing in .env file")

    client = BinanceFuturesClient(api_key, api_secret, logger)

    try:
        print("\n📌 Order Request Summary")
        print(vars(args))

        order = create_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Placed Successfully")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice", "N/A"))

    except Exception as e:
        print("\n❌ Order Failed:", e)

if __name__ == "__main__":
    main()