from OOPS_learning.Item import Item


class Phone(Item):  # inheritance - Phone extends Item
    all_phones = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken_phones should be positive number"
        self.broken_phones = broken_phones
        Phone.all_phones.append(self)

    def calculate_total_price(self):
        broken_price = self.broken_phones * self.__price
        return super().calculate_total_price() - broken_price

    def __repr__(self):
        return f"Phone('{self.name}', {self.__price}, {self.quantity}, {self.broken_phones})\n"

