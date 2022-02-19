import csv


class Item:
    pay_rate = 0.8  # It's called class variable.  Similar to static variable in Java
    all_items = []

    def __init__(self, name: str, price: float, quantity=0):
        assert len(name) > 0, f"Name shouldn't be empty!!"
        assert price >= 0, f"Price should be positive number"
        assert quantity >= 0, f"Quantity should be positive number"

        # self._name = name
        self.__name = name
        self.__price = price
        self.quantity = quantity
        print(f"{name} instance is created!!")

        Item.all_items.append(self)  # Adding the created instance to the all_item list

    def __print_discount_msg(self):
        print(f"Applying discount of {Item.pay_rate}")

    """
    This is to make name property is readOnly. 
    """
    @property
    def name(self):
        # return self._name    #Still accessible outside class using instance._name
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__print_discount_msg()
        """
        This below version also works, but if any instance has their own class variable modification, it won't work as
        expected as Item.pay_rate is always gives 0.8 

        """
        # self.price = self.price * Item.pay_rate
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value: float):
        self.__price = self.__price + (self.__price * increment_value)


    @name.setter    #setter for name property -> <propertyName>.setter
    def name(self, new_name):   #setter method name should match exactly to property name. set_name wont work
        self.__name = new_name


    def calculate_total_price(self):
        return self.__price * self.quantity

    """
    This is the class method - similar to static method. Using this method to instantiate 
    our instances from csv file.
    The default argument will be 'cls' in this case, not self
    Class methods are mostly used to instantiate objects from external sources. 
    """

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as items_csv_file:
            items_dict = csv.DictReader(items_csv_file)
            item_list = list(items_dict)
        for item in item_list:
            Item(name=item.get("name"), price=float(item.get("price")), quantity=int(item.get("quantity")))

    """
    This below one is the staticmethod which is similar to static methods in Java.
    https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
    """

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()  # it will return true if num is 1.0, 2.0 etc. return false if num like 1.1, 2.2 etc
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        """
        This method is kind of toString in Java. So we are overriding it
        TODO:  Check in google for difference between __repr__ and __str__ magic methods.

        self.__class__.__name__ will print the calling class name. Its a generic way..
        :return:
        """
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})\n"