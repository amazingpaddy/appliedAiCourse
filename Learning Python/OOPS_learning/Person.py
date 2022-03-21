

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age
    
    '''
    It is called when an object is garbage collected which happens 
    at some point after all references to the object have been deleted.
    '''
    def __del__(self):
        print("Object is being deleted...")
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"
    
    # This call function will trigger if we call object()
    def __call__(self):
        print("I am called..!!")


person = Person("Paddy", 32)
print(person)
print(f"Person name is - {person.name}")
print(f"Person age is - {person.age}")

#call magic method will be triggered.
person()