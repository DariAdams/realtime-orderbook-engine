
from decimal import Decimal
from order import Order


class OrderBook:
    def __init__(self):
        self.orders: dict[int, Order] = {}

    def add_order(self, order: Order) -> None:
        if order.order_id in self.orders:
            raise ValueError("Order ID already exists")

        self.orders[order.order_id] = order

    def cancel_order(self, order_id: int) -> None:
        if order_id not in self.orders:
            raise ValueError("Order not found")

        del self.orders[order_id]

    def get_best_bid(self) -> Decimal | None:
        return max(
            (
                order.price
                for order in self.orders.values()
                if order.side == "BUY"
            ),
            default=None,
        )

    def get_best_ask(self) -> Decimal | None:
        return min(
            (
                order.price
                for order in self.orders.values()
                if order.side == "SELL"
            ),
            default=None,
        )

    def get_spread(self) -> Decimal | None:
        bid = self.get_best_bid()
        ask = self.get_best_ask()

        if bid is None or ask is None:
            return None

        return ask - bid

    def get_depth(self, side: str) -> list[tuple[Decimal, int]]:
        if side not in ("BUY", "SELL"):
            raise ValueError("Side must be BUY or SELL")

        levels: dict[Decimal, int] = {}

        for order in self.orders.values():
            if order.side == side:
                levels[order.price] = (
                    levels.get(order.price, 0) + order.quantity
                )

        return sorted(
            levels.items(),
            key=lambda level: level[0],
            reverse=(side == "BUY"),
        )

    def snapshot(self) -> dict:
        return {
            "order_count": len(self.orders),
            "best_bid": self.get_best_bid(),
            "best_ask": self.get_best_ask(),
            "spread": self.get_spread(),
            "bids": self.get_depth("BUY"),
            "asks": self.get_depth("SELL"),
        }
