from overrides import overrides

from bonus.Pet import Pet
from bonus.model.Animal import Animal


class Cat(Animal,Pet):
    def __init__(self, legs, name):
        Animal.__init__(self, legs)
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    @overrides
    def play(self):
        print("I am a cat and I am playing!")
    @overrides
    def eat(self):
        print("I'm a cat and I'm eating")
