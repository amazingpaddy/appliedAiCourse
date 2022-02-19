class FooBase(object):
    name = "FooBase"

    def foo(self):
        print('         Base.foo() begins')
        print("         My name is: %s" % self.name)
        print("         My super's name is not available")
        print('         Base.foo() ends')


class A(FooBase):
    name = "A"

    def foo(self):
        print('     A.foo() begins')
        print("     My name is: %s" % self.name)
        print("     My super's name is: %s" % super(A, self).name)
        print("     A.__mro__ is %s" % str(A.__mro__))
        super(A, self).foo()
        print('     A.foo() ends')


class B(FooBase):
    name = "B"

    def foo(self):
        print('     B.foo() begins')
        print("     My name is: %s" % self.name)
        print("     My super's name is: %s" % super(B, self).name)
        print("     B.__mro__ is %s" % str(B.__mro__))
        super(B, self).foo()
        print('     B.foo() ends')


class C(A, B):
    name = "C"

    def foo(self):
        print('C.foo() begins')
        print("My name is: %s" % self.name)
        print("My super's name is: %s" % super(C, self).name)
        print("C.__mro__ is %s" % str(C.__mro__))
        super(C, self).foo()
        print('C.foo() ends')


# print("We will call A.foo()")
# A().foo()
#
# print("We will call C.foo()")

C().foo()
