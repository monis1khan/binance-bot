from bot.validators import validate_inputs

def create_order(client, symbol, side, order_type, quantity, price=None):
    validate_inputs(order_type, price)

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    return client.place_order(**params)