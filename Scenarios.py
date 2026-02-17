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

#Drawing tool - Prototype Pattern
import copy

class ShapesPrototype:
    def clone(self):
        pass

class Square(ShapesPrototype):
    def clone(self):
        return copy.copy(self)
    
    def __str__(self):
        return "Square"

class Circle(ShapesPrototype):
    def clone(self):
        return copy.copy(self)
    
    def __str__(self):
        return "Circle"

class Triangle(ShapesPrototype):
    def clone(self):
        return copy.copy(self)
    
    def __str__(self):
        return "Triangle"
    
square_prototype = Square()
circle_prototype = Circle()
triangle_prototype = Triangle()
shapes = []

for _ in range(5):
    shapes.append(square_prototype.clone())
for _ in range(3):
    shapes.append(circle_prototype.clone())
for _ in range(4):
    shapes.append(triangle_prototype.clone())
for idx, shape in enumerate(shapes, start=1):
    print(f"Shape {idx}: {shape}")

#Global Counter - Singleton Pattern
class GlobalCounter:
    _instance = None
    _count = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalCounter, cls).__new__(cls)
            cls._count = 0
        return cls._instance

    def increment(self):
        self._count += 1
        print(f"Counter incremented to {self._count}")

    def get_count(self):
        return self._count

counter1 = GlobalCounter()
counter2 = GlobalCounter()

counter1.increment()
counter2.increment()
counter1.increment()

print("Final Count:", counter2.get_count())

#Greeting Card Personalization - Prototype Pattern
import copy

class CardPrototype:
    def clone(self):
        pass


class GreetingCard(CardPrototype):
    def __init__(self, design, message="", theme=""):
        self.design = design
        self.message = message
        self.theme = theme

    def clone(self):
        return copy.copy(self)

    def __str__(self):
        return (
            f"Design: {self.design}\n"
            f"Theme: {self.theme}\n"
            f"Message: {self.message}\n"
            "-------------------------"
        )

birthday_template = GreetingCard("Birthdaycore Design")
wedding_template = GreetingCard("Floral Design")
holiday_template = GreetingCard("Summer Xmas Design")

cards = []

card1 = birthday_template.clone()
card1.message = "Happy Birthday [Name]!"
card1.theme = "Colourful"
cards.append(card1)

card2 = wedding_template.clone()
card2.message = "Congratulations on your special day!"
card2.theme = "White & Gold"
cards.append(card2)

card3 = holiday_template.clone()
card3.message = "Merry Christmas!"
card3.theme = "Red & Green"
cards.append(card3)

for idx, card in enumerate(cards, start=1):
    print(f"Card {idx}")
    print(card)