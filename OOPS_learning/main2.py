from Item import Item

item1 = Item("MyItem", 50, 5)
print(f"Name of the item1 is {item1.name}")
# item1.name = "NotYourItem"   # -- > will throw error
#item1._name = "NotYourItem"   # You can still force change the name using this.
# Below Wont throw any error but name wont change the value as well but it will create its own variable
# item1.__name = "NotYourItem"
print(f"Name of the item1 is {item1.name}")
# print(f"__Name of the item1 is {item1.__name}") #This will throw error since there is no attribute __name

item1.name = "MyNewItem"
print(f"Name of the item1 post change using setter - {item1.name}")
print(f"Price before applied the increment - {item1.price}")
item1.apply_increment(0.2)
print(f"Price after applied the increment - {item1.price}")
item1.apply_discount()
print(f"Price after applied the discount - {item1.price}")

item1._Item__print_discount_msg()  #You still call private method of the class Item using this convention
print(dir(item1))


