
import asyncio
import random
from decimal import Decimal


async def generate_market_data(count=20, delay=0.1):
    rng = random.Random(42)

    for order_id in range(1, count + 1):
        side = rng.choice(["BUY", "SELL"])
        price_cents = rng.randint(9500, 10500)
        quantity = rng.randint(1, 100)

        yield {
            "order_id": order_id,
            "side": side,
            "price": str(
                Decimal(price_cents) / Decimal(100)
            ),
            "quantity": quantity,
        }

        await asyncio.sleep(delay)
