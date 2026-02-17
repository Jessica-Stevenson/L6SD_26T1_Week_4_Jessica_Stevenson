#President's Official Pen - Singleton Pattern
class PresidentPen:
    _instance = None
    _pen = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PresidentPen, cls).__new__(cls) 
            cls._pen = "Le super important pen"
        return cls._instance
    def use_pen (self, president_name):
        print(f"{president_name} is using the {self._pen}")

pen1 = PresidentPen()
pen2 = PresidentPen()
pen1.use_pen("John smith")
pen2.use_pen("Desotryer110")

#Car Manufacturing Plant - Factory Pattern
class Car:
    def make(self):
        pass

class HondaCivic (Car):
    def make(self):
        print("Making Honda Civic")

class MonsterTrcuk1000 (Car):
    def make(self):
        print("Making Monster Trcuk 1000")

class LeCar (Car):
    def make(self):
        print("Making Le Car")

class CarFactory:
    def create_car(self, car_type): 
        if car_type == "HondaCivic":
            return HondaCivic()
        elif car_type == "MonsterTrcuk1000":
            return MonsterTrcuk1000()
        elif car_type == "LeCar":
            return LeCar()
        
factory = CarFactory()
Car1 = factory.create_car("HondaCivic") 
Car2 = factory.create_car("MonsterTrcuk1000") 
Car3 = factory.create_car("LeCar")

cars = [Car1, Car2, Car3]

for car in cars:
    car.make()