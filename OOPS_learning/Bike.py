from OOPS_learning.Vehicle import Vehicle


class Bike(Vehicle):


    def go(self):
        print("Driving Bike... ")

    def do_print(self):
        print("Hello")


bike = Bike()
bike.go()