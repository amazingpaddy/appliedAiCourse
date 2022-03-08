
class Config:
    def __init__(self, name):
        self.__name = name

    def __repr__(self) -> str:
        return f"name = {self.__name}"

    @property
    def name(self):
        # return self._name    #Still accessible outside class using instance._name
        return self.__name