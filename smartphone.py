# Smartphone Class Assignment
# Author: Bridie Maugham Dibora

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        # I initialize attributes when creating an object
        self.__brand = brand  # Encapsulated attribute
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    # Encapsulation: Getter and Setter for Brand
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def call(self, number):
        print(f"{self.__brand} {self.model} is calling {number}...")

    def charge(self):
        print(f"{self.__brand} {self.model} is charging.")

    def specs(self):
        print(f"Brand: {self.__brand}, Model: {self.model}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours")


# Subclass with Inheritance
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery_life, strap_type):
        # I call the parent constructor
        super().__init__(brand, model, storage, battery_life)
        self.strap_type = strap_type

    def specs(self):
        # I override the parent method to include strap type
        print(f"Smartwatch: {self.get_brand()}, Model: {self.model}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hrs, Strap: {self.strap_type}")


# Testing the Classes
phone = Smartphone("Apple", "iPhone 15 Pro", 256, 20)
watch = Smartwatch("Apple", "Watch Series 9", 32, 18, "Leather")

phone.specs()
phone.call("+254712345678")
watch.specs()
