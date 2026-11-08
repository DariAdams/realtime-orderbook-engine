
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Order:
    order_id: int
    side: str
    price: Decimal
    quantity: int

    def __post_init__(self):
        if type(self.order_id) is not int or self.order_id < 1:
            raise ValueError("Order ID must be a positive integer")

        if self.side not in ("BUY", "SELL"):
            raise ValueError("Side must be BUY or SELL")

        if not isinstance(self.price, Decimal):
            raise TypeError("Price must be a Decimal")

        if not self.price.is_finite() or self.price <= 0:
            raise ValueError("Price must be positive and finite")

        if type(self.quantity) is not int or self.quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
