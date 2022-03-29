
class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value != "Bob":
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    def say_hello(self):
        say_hello()

    @staticmethod
    def static_func():
        print("Hey I am static method!!")

    @classmethod
    def class_method(cls):
        print("Hey I am class method!!")


def say_hello():
    print("Hello..!!")

paddy = Person("Paddy", 40, "male")
print(f"Name of the paddy - {paddy.name}")
print(f"age of the paddy - {paddy.age}")

paddy.age = 30
paddy.name = "Bob"
print(f"Name of the paddy after change - {paddy.name}")
print(f"Age of the paddy after change - {paddy.age}")

paddy.say_hello()

Person.static_func()
paddy.static_func()
Person.class_method()
paddy.class_method()




