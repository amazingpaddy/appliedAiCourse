from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def say_hello(): pass

class Student(IPerson):

    def say_hello(self):
        print("I am a student!!")

class ProxyStudent(IPerson):

    def __init__(self) -> None:
        super().__init__()
        self.__student = Student()
    
    def say_hello(self):
        print("I am a proxy student!!")
        self.__student.say_hello()

s1 = Student()
s1.say_hello()
s2 = ProxyStudent()
s2.say_hello()
