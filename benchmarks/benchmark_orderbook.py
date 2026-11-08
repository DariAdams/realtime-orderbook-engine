
import sys
import time
from decimal import Decimal
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1])
)

from order import Order
from order_book import OrderBook


def benchmark(total_orders=10000):
    book = OrderBook()

    start = time.perf_counter()

    for i in range(1, total_orders + 1):
        side = "BUY" if i % 2 == 0 else "SELL"
        price = Decimal(10000 + i % 1000) / 100

        book.add_order(
            Order(i, side, price, 10)
        )

    insert_time = time.perf_counter() - start

    start = time.perf_counter()

    for _ in range(100):
        book.get_best_bid()
        book.get_best_ask()

    lookup_time = time.perf_counter() - start

    print(f"Orders: {total_orders:,}")
    print(f"Insertion time: {insert_time:.6f} seconds")
    print(f"Best-price queries (200): {lookup_time:.6f} seconds")
    print(f"Best Bid: {book.get_best_bid()}")
    print(f"Best Ask: {book.get_best_ask()}")


if __name__ == "__main__":
    benchmark()
