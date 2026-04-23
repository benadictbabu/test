num=20
print("type of num:", type(num))

num=2.0
print("type of num:", type(num))

num={"key":20}
print("type of num:", type(num))

num=[1,2,3,4,5]
print("type of num:", type(num))

num=(1,2,3,4,5)
print("type of num:", type(num))

def hello():
    print("Hello, World!")  

print("type of num:", type(hello))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return(f"Hello, my name is {self.name} and I am {self.age} years old.")
    def __repr__(self):
        return f"Person(name='{self.name!r}', age={self.age!r})"

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1)         #Person(name='Alice', age=30)
print(p2.greet())  #Hello, my name is Bob and I am 25 years old.
print(p2.name, p2.age)   #Bob 25

