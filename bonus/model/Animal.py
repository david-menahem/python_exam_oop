from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, legs: int):
       self.legs = legs

    def walk(self):
        print("I'm walking!")

    @abstractmethod
    def eat(self):
        pass