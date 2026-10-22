from abc import ABC, abstractmethod
import math


class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.__age = age

    def get_age(self):
        return self.__age


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    print("=== 1. Инкапсуляция ===")
    p = Person()
    p.set_age(25)
    print(p.get_age())  # 25

    try:
        p.set_age(-5)
    except ValueError as error:
        print("Ошибка:", error)

    print("\n=== 2. Наследование ===")
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(dog.name, dog.speak())
    print(cat.name, cat.speak())

    print("\n=== 3. Полиморфизм ===")
    car = Car()
    bike = Bicycle()
    print(move(car))
    print(move(bike))

    print("\n=== 4. Абстракция ===")
    rect = Rectangle(10, 5)
    circle = Circle(7)
    print(rect.area())
    print(round(circle.area(), 2))