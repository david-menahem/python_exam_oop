from Giftable import Giftable
from enums.CustomerType import CustomerType


class Customer:
    def __init__(self, id, first_name, last_name, email, delivery_address, customer_type: CustomerType,
                 discount,favorite_items, gift):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.__delivery_address = delivery_address
        if isinstance(customer_type,CustomerType):
            self.customer_type = customer_type
        self.discount = discount
        self.favorite_items = favorite_items
        self.gift = gift


    @property
    def delivery_address(self):
        return self.delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        self.delivery_address = delivery_address

    def add_to_favorites_from_order(self,items):
        for item in items:
            exists = False
            for fav_item in self.favorite_items:
                if item == fav_item:
                    exists = True
            if not exists:
                self.favorite_items.append(item)

    def add_to_favorites(self,items):
        for item in items:
            exists = False
            for fav_item in self.favorite_items:
                if item == fav_item:
                    exists = True
            if not exists:
                self.favorite_items.append(item)

    def remove_from_favorites(self,items):
        for item in items:
            exists = False
            for fav_item in self.favorite_items:
                if item == fav_item:
                    exists = True
            if exists:
                self.favorite_items.remove(item)

    def take_gift(self,gift):
        if isinstance(gift,Giftable):
            self.gift = gift
