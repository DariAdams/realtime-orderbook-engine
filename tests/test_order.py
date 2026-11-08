
from decimal import Decimal

import pytest

from order import Order


def test_create_valid_order():
    order = Order(1, "BUY", Decimal("100.50"), 10)

    assert order.order_id == 1
    assert order.side == "BUY"
    assert order.price == Decimal("100.50")
    assert order.quantity == 10


def test_invalid_side():
    with pytest.raises(ValueError):
        Order(1, "HOLD", Decimal("100"), 10)


def test_negative_price():
    with pytest.raises(ValueError):
        Order(1, "BUY", Decimal("-5"), 10)


def test_zero_quantity():
    with pytest.raises(ValueError):
        Order(1, "SELL", Decimal("100"), 0)


def test_float_price_rejected():
    with pytest.raises(TypeError):
        Order(1, "BUY", 100.5, 10)
