from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def say_hello(): pass


class Student(IPerson):

    def __init__(self): pass

    def say_hello(self):
        print("I am a student..!!")


class Teacher(IPerson):

    def __init__(self): pass

    def say_hello(self):
        print("I am a teacher..!!")


class PersonFactory:
    @staticmethod
    def build_person(who: str) -> IPerson:
        if who == 'student':
            return Student()
        elif who == 'teacher':
            return Teacher()
        else:
            raise TypeError(f"Type - {who} is not defined")


person1 = PersonFactory.build_person("student")
person1.say_hello()
person2 = PersonFactory.build_person("teacher")
person2.say_hello()
# person3 = PersonFactory.build_person("dummy")
# person3.say_hello()
