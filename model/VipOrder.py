from overrides import overrides

from model.enums.CustomerType import CustomerType
from model.Order import Order


class VipOrder(Order):
    def __init__(self, id, name, items, order_customer, payment_type, order_date):
        super().__init__(id, name, items, order_customer, payment_type, order_date)
        self.order_total_price = self.total_price()

    @overrides
    def total_price(self):
        if self.order_customer.customer_type == CustomerType.VIP:
            total_price = 0
            discount = self.order_customer.discount
            for item in self.items:
                price = item.item_price
                total_price += price - price*discount/100
            return total_price
        else:
            raise Exception("You are not a VIP customer!!!")