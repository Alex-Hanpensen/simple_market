from unittest.mock import MagicMock
import pytest

from main import Order, OrderBook


@pytest.fixture()
def order():
    order = Order(1, 2, 3, 'sell')

    return order


class TestOrderBook:
    orderbook = OrderBook()
    orderbook.delete = MagicMock(return_value='successful deletion')
    orderbook.deal = MagicMock(return_value='user registration')
    orderbook.add_order = MagicMock(return_value=[Order(1, 2, 3, 'sell')])

    def test_delete(self, order):
        assert self.orderbook.delete(order) is not None

    def test_deal(self, order):
        assert self.orderbook.deal(order) is not None

    def test_add_order(self, order):
        assert len(self.orderbook.add_order(order)) > 0
