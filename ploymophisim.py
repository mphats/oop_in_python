class Animal:  
    def move(self):  
        raise NotImplementedError("Subclasses must implement this method.")  


class Dog(Animal):  
    def move(self):  
        print("The dog is running.")  


class Cat(Animal):  
    def move(self):  
        print("The cat is jumping.")  


class Vehicle:  
    def move(self):  
        raise NotImplementedError("Subclasses must implement this method.")  


class Car(Vehicle):  
    def move(self):  
        print("Driving 🚗")  


class Plane(Vehicle):  
    def move(self):  
        print("Flying ✈️")  


# Example usage  
def polymorphism_demo():  
    # Animals  
    dog = Dog()  
    cat = Cat()  

    # Vehicles  
    car = Car()  
    plane = Plane()  

    # Demonstrate polymorphism  
    for animal in (dog, cat):  
        animal.move()  

    for vehicle in (car, plane):  
        vehicle.move()  

polymorphism_demo()