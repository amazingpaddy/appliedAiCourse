from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def print_data(): pass

class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton.__instance = PersonSingleton()
            return PersonSingleton.__instance
        else:
            return PersonSingleton.__instance
    
    def __init__(self) -> None:
        if PersonSingleton.__instance != None: 
            return PersonSingleton.__instance
        else:
            PersonSingleton.__instance = self
    
    def print_data(self):
        print(f"Name --> ")
    

p = PersonSingleton.get_instance()
print(p)
p1 = PersonSingleton.get_instance()
print(p1)

