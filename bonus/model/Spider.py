from overrides import overrides

from bonus.model.Animal import Animal


class Spider(Animal):

    def __init__(self,legs):
        super().__init__(legs)

    @overrides
    def eat(self):
        print("I'm a spider and I'm eating!")