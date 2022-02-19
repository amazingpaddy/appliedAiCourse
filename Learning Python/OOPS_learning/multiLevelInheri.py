class Organism:
    alive = True

    def say_hello(self):
        print("Hello from Organism!!")


class Animal(Organism):
    def say_hello(self):
        print("Hello from Animal!!")


class Human(Animal):
    def say_hello(self):
        super().say_hello()  # Calling parent method
        Organism.say_hello(self)  # Calling grandparent method
        super(Animal, self).say_hello()  # Another way of calling Grandparent method..


human = Human()
human.say_hello()


