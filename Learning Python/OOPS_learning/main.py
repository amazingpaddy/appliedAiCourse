from OOPS_learning.Item import Item
from OOPS_learning.Phone import Phone

# Access class attribute using class name.
print(f"Class variable pay_rate = {Item.pay_rate}")
iPhone = Item("Iphone", 888, 6)
print(
    f"Class variable accessed from iphone instance - {iPhone.pay_rate}")  # We can access class attribute using
# instance of the class as well
# Dummy = Item("", 888, 6)

# iPhone.name = "iPhone"  # We can just randomly create instance variable just like this.
# iPhone.quantity = 5
# iPhone.price = 888

# print(type(iPhone))
# print(type(iPhone.name))

print(f"Price before applying the discount - {iPhone.calculate_total_price()}")
iPhone.apply_discount()
print(f"Price after applying the discount - {iPhone.calculate_total_price()}")
iPhone.__price = 1000
print(f"Total iphone Price after price increase is {iPhone.calculate_total_price()}")

# We can have the class variable at instance level and modify the value specific to instance.

laptop = Item("Laptop", 2000, 2)
laptop.pay_rate = 0.7  # Changing the class variable at instance level.
print(f"Class variable pay_rate at laptop instance level - {laptop.pay_rate}")
print(f"Class variable pay_rate at class level - {Item.pay_rate}")
print(f"Class variable pay_rate at iphone instance level - {Item.pay_rate}")

cable = Item("Cable", 100, 3)
mouse = Item("Mouse", 100, 3)
keyboard = Item("KeyBoard", 100, 3)

print(f"Total items - {len(Item.all_items)}")
print(Item.all_items)

Item.instantiate_from_csv()
print(Item.all_items)

pixel = Phone("Google Pixel", 600.0, 4, 1)
galaxyPlus = Phone("Samsung Galaxy Plus", 785.25, 7, 2)
# print(Phone.all_items)
print(Item.all_items)
print(f"Pixel phone total price {pixel.calculate_total_price()}")
print(f"Galaxy phone total price {galaxyPlus.calculate_total_price()}")
