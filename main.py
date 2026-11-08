from order import Order
from order_book import OrderBook

book = OrderBook()

order1 = Order(1, "BUY", 100.0, 10)
order2 = Order(2, "BUY", 105.0, 5)
order3 = Order(3, "SELL", 110.0, 8)

book.add_order(order1)
book.add_order(order2)
book.add_order(order3)

print(book.orders)

book.cancel_order(1)

print(book.orders)