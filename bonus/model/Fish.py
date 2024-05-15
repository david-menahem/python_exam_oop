from overrides import overrides

from bonus.Pet import Pet
from bonus.model.Animal import Animal


class Fish(Animal, Pet):
    def __init__(self, legs, name):
        Animal.__init__(self, legs)
        self.name = name

    @overrides
    def get_name(self):
        return self.name

    @overrides
    def set_name(self, name):
        self.name = name

    @overrides
    def play(self):
        print("I am a fish and I am playing")

    @overrides
    def eat(self):
        print("I am a fish and I am eating")

    @overrides
    def walk(self):
        print("I am a fish I can't walk")
