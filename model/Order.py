from abc import ABC, abstractmethod

from model.enums.PaymentType import PaymentType


class Order(ABC):
    @abstractmethod
    def __init__(self, id, name, items, order_customer,
                 payment_type: PaymentType, order_date):
        self.id = id
        self.name = name
        self.items = items
        self.order_customer = order_customer
        if isinstance(payment_type, PaymentType):
            self.payment_type = payment_type
        self.order_date = order_date
        order_customer.add_to_favorites(items)

    @abstractmethod
    def total_price(self):
        pass
