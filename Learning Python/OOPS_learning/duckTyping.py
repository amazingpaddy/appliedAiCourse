class Duck:
    def walk(self):
        print("Duck is walking..")

class Chicken:
    def walk(self):
        print("Chicken is walking..")

class Person:
    def catch(self, duckObj: Duck):
        duckObj.walk()

duck = Duck()
chicken = Chicken()
person = Person()

#Below both methods works since both duck and chicken has walk method
person.catch(duck)
person.catch(chicken)  #still works..