from bonus.model.Cat import Cat
from bonus.model.Fish import Fish
from bonus.model.Spider import Spider

if __name__ == '__main__':
    cat = Cat(4,"bunjie")
    fish = Fish(0,"nimo")
    spider = Spider(8)

    cat.set_name("prince")
    print(cat.get_name())
    cat.play()
    cat.walk()
    cat.eat()

    fish.play()
    fish.walk()
    print((fish.get_name()))
    fish.set_name("eli")
    print(fish.get_name())
    fish.play()

    spider.eat()
    spider.walk()