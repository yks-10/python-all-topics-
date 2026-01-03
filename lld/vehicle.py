class Vechicle:
    def __init__(self, brand, speed):
        self.brand = brand 
        self.speed = speed 

    def display_info(self):
        return f"Brand {self.brand} speed is {self.speed}"

    def accelerate(self):
        self.speed += 10
        return f"Speed of {self.brand} is increased to {self.speed}"


class Car(Vechicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed) 
    
    def accelerate(self):
        self.speed += 20
        return f"Speed of {self.brand} is increased to {self.speed}"

class Bike(Vechicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed) 
    
    def accelerate(self):
        self.speed += 15
        return f"Speed of {self.brand} is increased to {self.speed}"


def test_accelerate(obj):
    print(obj.accelarate())

obj = [Car("AUDI", 130), Bike("DUKE", 100)]
for i in obj:
    print(i.accelerate())
