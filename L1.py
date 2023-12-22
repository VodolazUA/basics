class Vehicle:
    def __init__(self, name):
        self.name = name
        print(f"New vehicle has been created: <{name}>")

    def __str__(self):
        return self.name


class Car(Vehicle):

    def drive(self):
        print(f"{self.name} is moving.")
    
    def stop(self):
        print(f"{self.name} has stopped.")
    
    def change_gear(self, new_gear):
        print(f"Current gear is {new_gear}.")

    def honk(self):
        print("Beep beep!!!")
    
    

class ElectricCar(Car):
    
    def charge(self):
        print(f"{self.name} has been charged.")
    
    def drive(self):
        print(f"{self.name} is moving (eco).")


class GasCar(Car):
    
    def fill_up(self):
        print(f"{self.name} has been filled up.")


if __name__ == "__main__":
    
    print("-----------")

    car1 = GasCar("Golf GTI")
    
    car1.drive()
    car1.change_gear(2)
    car1.change_gear(3)
    car1.stop()
    car1.honk()
    car1.fill_up()

    print("-----------")

    car1 = ElectricCar("Audi e-tron")
    car1.drive()
    car1.change_gear("Drive mode")
    car1.stop()
    car1.change_gear("Reverse mode")
    car1.stop()
    car1.honk()
    car1.charge()
