from abc import ABC

from overrides import overrides

from model.Item import Item
from model.Order import Order


class RegularOrder(Order):
    def __init__(self, id, name, items, order_customer, payment_type, order_date):
        super().__init__(id, name, items, order_customer, payment_type, order_date)
        self.order_total_price = self.total_price()

    @overrides
    def total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.item_price
        return total_price
