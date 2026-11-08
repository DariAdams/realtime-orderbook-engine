
import asyncio
import json
from decimal import Decimal

from websockets.asyncio.client import connect

from order import Order
from order_book import OrderBook


async def consume_market_data(
    url="ws://localhost:8765",
    max_messages=20,
):
    book = OrderBook()

    async with connect(url) as websocket:
        for _ in range(max_messages):
            message = await websocket.recv()
            data = json.loads(message)

            order = Order(
                order_id=data["order_id"],
                side=data["side"],
                price=Decimal(data["price"]),
                quantity=data["quantity"],
            )

            book.add_order(order)

            print(
                "Best Bid:", book.get_best_bid(),
                "| Best Ask:", book.get_best_ask(),
            )

    return book


if __name__ == "__main__":
    asyncio.run(consume_market_data())
