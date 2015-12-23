import json
import random

import settings
import stockfighter


def stat(text, resp):
    print(text)
    print(json.dumps(resp.json(), indent=2))


sf = stockfighter.Stockfighter(
    account="AAH50221105",
    venue="CELUEX",
    api_key=settings.api_key,
)

stock = "HRE"

sf.get_latest_quote(stock)
sf.get_orderbook(stock)

total_fills = 100000

while True:
    # dumb block-order fill
    quote = sf.get_latest_quote(stock)
    stat("quote", quote)

    qty = random.randint(1, 50000)
    price = random.randint(6500, 6600)
    print("we asked for {0} at {1}".format(
        qty,
        price,
    ))
    buy_resp = sf.place_order(
        stock=stock,
        order_type="limit",
        quantity=qty,
        price=price,
        direction="buy",
    )
    stat("buy:", buy_resp)
