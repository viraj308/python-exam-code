# encapsulation examples by showing protected and private menbers

class Base:
    def __init__(self):

        # protected member, prefix the name with a single underscore _
        self._a = 10

        # private member, prefix the name with double underscore __
        self.__b = 20

        print("hello world")
        print(self._a)
        print(self.__b)


class Derived(Base):
    def __init__(self):
        print("bye bye world")
        Base.__init__(self)
        self._a = 100
        print(self._a)
        print(self.__b)


obj1 = Derived()
