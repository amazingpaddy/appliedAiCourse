import csv

class Item:
    pay_rate = 0.8  # It's called class variable.  Similar to static variable in Java
    all_items = []

    def __init__(self, name: str, price: float, quantity=0):
        assert len(name) > 0, f"Name shouldn't be empty!!"
        assert price >= 0, f"Price should be positive number"
        assert quantity >= 0, f"Quantity should be positive number"

        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"{name} instance is created!!")

        Item.all_items.append(self)  # Adding the created instance to the all_item list

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        print(f"Applying discount of {Item.pay_rate}")
        """
        This below version also works, but if any instance has their own class variable modification, it won't work as
        expected as Item.pay_rate is always gives 0.8 
        
        """
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

    """
    This is the class method - similar to static method. Using this method to instantiate 
    our instances from csv file.
    The default argument will be 'cls' in this case, not self
    """

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as items_csv_file:
            items_dict = csv.DictReader(items_csv_file)
            item_list = list(items_dict)
        for item in item_list:
            Item(name=item.get("name"), price=float(item.get("price")), quantity=int(item.get("quantity")))

    def __repr__(self):
        """
        This method is kind of toString in Java. So we are overriding it
        TODO:  Check in google for difference between __repr__ and __str__ magic methods.
        :return:
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})\n"


print(f"Class variable pay_rate = {Item.pay_rate}")  # Access class attribute using class name.
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
iPhone.price = 1000
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


