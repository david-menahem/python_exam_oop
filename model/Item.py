class Item:
    def __init__(self,id, item_name, item_price):
        self.id = id
        self.item_name = item_name
        self.item_price = item_price

    def __eq__(self, other):
        if isinstance(other,Item):
            return self.item_name == other.item_name
        return False

