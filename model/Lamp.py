from overrides import overrides

from Giftable import Giftable


class Lamp(Giftable):
    @overrides
    def open_gift(self):
        print("Congratulations, you got a new gift!")

