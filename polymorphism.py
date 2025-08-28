# Polymorphism with Vehicles
# Author: Bridie Maugham Dibora

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Testing Polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each vehicle moves differently
