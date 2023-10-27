import datetime
from random import choice, choices


class Order:
    def __init__(self, order_id, quantity, price, order_type):
        self.order_id = order_id
        self.timestamp = datetime.datetime.now()
        self.quantity = quantity
        self.price = price
        self.order_type = order_type

    def __repr__(self):
        return f'order_id {self.order_id}, on {self.order_type}'


class OrderBook:
    def __init__(self):
        self.active_orders = []
        self.history_orders = []

    def add_order(self, order):
        self.active_orders.append(order)
        print(
            f'there was an order registration, the implementation will be automatic as soon as we find the right price!')

    def delete(self, order):
        index = self.active_orders.index(order)
        del self.active_orders[index]
        print('the transaction has taken place the order will be automatically deleted from the order book')

    def change(self, old_order, new_order):
        index = self.active_orders.index(old_order)
        self.active_orders[index] = new_order

    def buy_expensive(self):
        buy_order = max(self.active_orders, key=lambda x: x.prace)
        self.delete(buy_order)

    def sell_cheap(self):
        sell_ch = max(self.active_orders, key=lambda x: x.prace)
        self.delete(sell_ch)

    def check(self, order, sellers):
        for sell in sellers:
            if sell.price == order.price:
                self.history_orders.append([order, sell])
                self.delete(sell)
                return True
        return False

    def deal(self, order):
        if order.order_type == 'purchase':
            if self.check(order, filter(lambda x: x.order_type == 'sale', self.active_orders)):
                return self.history_orders

        else:
            if self.check(order, filter(lambda x: x.order_type == 'purchase', self.active_orders)):
                return self.history_orders
        self.add_order(order)


def get_start():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return [Order(choice(numbers), choice(numbers), choice(numbers), choice(['purchase', 'sale'])) for _ in range(20)]


if __name__ == '__main__':
    orderbook = OrderBook()
    [orderbook.deal(order) for order in get_start()]
    print(f'list of valid applications {orderbook.active_orders}')
    print(f'transaction history {orderbook.history_orders}')
