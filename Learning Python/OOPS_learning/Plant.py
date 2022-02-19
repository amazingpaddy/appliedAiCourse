# https://stackoverflow.com/questions/71181294/python3-modifying-read-only-property-not-throwing-attributeerror?noredirect=1#71181408
class Plant:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name


table_rose = Plant("Table Rose")
print(f"Name of the plant - {table_rose.name}")

#trying the change the name.. Expecting Attribute error in the below line.
table_rose.__name = "Croutons"

print(f"Name of the plant - {table_rose.name}")  #name didnt change..

print(f"Name of the plant - {table_rose.__name}") #It prinits Croutons.. Confusing how python handling things.
