# polymorphism means "many forms" and refers to the python's functions/methods/operators that has the same name and can be
# executed on many objects and classes

# example would be the python's len function

# 1. function polymorphism

a = "love you"
print(len(a))

myTuple = ("orange", "red")
print(len(myTuple))

mydict = {
    "name": "viraj",
    "age": 20,
    "favColor": "white"
}
print(len(mydict))

# 2. class polymorphism


class Akane:
    def slash():
        print("red slash")


class Midori:
    def slash():
        print("green slash")


class Shiro:
    def slash():
        print("white slash")


obj1 = Akane
obj2 = Midori
obj3 = Shiro

for x in (obj1, obj2, obj3):
    x.slash()

# Inheritence class polymorphism


class Vehicle:
    def drive(self):
        print("move")


class Car(Vehicle):
    def drive(self):
        print("Run")


class Plane(Vehicle):
    def drive(self):
        print("Fly")


vehicle = Vehicle()
car = Car()
plane = Plane()


for x in (vehicle, car, plane):
    x.drive()
