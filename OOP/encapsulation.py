class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  #private property

p1 = Person("Emily", 25)
print(p1.name)
print(p1._Person__age)