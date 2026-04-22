from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    
class defender(Car):
    def mileage(self):
        print('th mileage is 7km/l')

class tiago(Car):
    def mileage(self):
        print('the mileage is 13km/l')

class pajero(Car):
    def mileage(self):
        print('the mileage is 10km/l')

d = defender()
d.mileage()

i= tiago()
i.mileage() 