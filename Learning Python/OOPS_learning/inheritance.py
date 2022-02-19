class Animal:
    alive = True

    def eat(self):
        print(f"{self.__class__.__name__} is eating!!!")

    def sleep(self):
        print(f"{self.__class__.__name__} is sleeping!!!")

class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
