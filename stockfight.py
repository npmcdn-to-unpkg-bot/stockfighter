import settings
import stockfighter

sf = stockfighter.Stockfighter(
    account="",
    venue="",
    api_key=settings.api_key,
)

sf.get_latest_quote("XIXO")
sf.get_orderbook("XIXO")
sf.place_order(
    stock="XIXO",
    order_type="limit",
    quantity=1000,
    price=5900,
    direction="buy",
)
