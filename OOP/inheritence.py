# parent class
class Vehicle:
    def vehicle_info(self):
        print("inside vehicle class")

# child class
class Car(Vehicle):
    def car_info(self):
        print("inside car class")

c1 = Car()
#access vehicle info using car object
c1.vehicle_info()  # inherited method from Vehicle class
c1.car_info()      # method from Car class