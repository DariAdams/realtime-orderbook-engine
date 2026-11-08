
from decimal import Decimal

import pytest

from order import Order
from order_book import OrderBook


@pytest.fixture
def book():
    order_book = OrderBook()

    order_book.add_order(
        Order(1, "BUY", Decimal("100"), 10)
    )
    order_book.add_order(
        Order(2, "BUY", Decimal("105"), 5)
    )
    order_book.add_order(
        Order(3, "SELL", Decimal("110"), 8)
    )
    order_book.add_order(
        Order(4, "SELL", Decimal("108"), 12)
    )

    return order_book


def test_best_bid(book):
    assert book.get_best_bid() == Decimal("105")


def test_best_ask(book):
    assert book.get_best_ask() == Decimal("108")


def test_spread(book):
    assert book.get_spread() == Decimal("3")


def test_cancel_order(book):
    book.cancel_order(2)

    assert book.get_best_bid() == Decimal("100")


def test_duplicate_order(book):
    with pytest.raises(ValueError):
        book.add_order(
            Order(1, "BUY", Decimal("99"), 10)
        )


def test_cancel_missing_order(book):
    with pytest.raises(ValueError):
        book.cancel_order(999)


def test_empty_book():
    book = OrderBook()

    assert book.get_best_bid() is None
    assert book.get_best_ask() is None
    assert book.get_spread() is None


def test_aggregated_depth(book):
    book.add_order(
        Order(5, "BUY", Decimal("105"), 7)
    )

    assert book.get_depth("BUY") == [
        (Decimal("105"), 12),
        (Decimal("100"), 10),
    ]
