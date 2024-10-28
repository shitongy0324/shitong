class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = 0
        self.odometer = 0

    def set_speed(self, speed):
        if speed <= self.max_speed:
            self.current_speed = speed
        else:
            self.current_speed = self.max_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.odometer += distance


class ElectricCar(Car):
    def __init__(self, registration, max_speed, battery_capacity):
        super().__init__(registration, max_speed)
        self.battery_capacity = battery_capacity

    def print_information(self):
        print(f"Electric Car {self.registration}: Max Speed = {self.max_speed} km/h, "
              f"Battery Capacity = {self.battery_capacity} kWh, Odometer = {self.odometer} km")


class GasolineCar(Car):
    def __init__(self, registration, max_speed, fuel_tank_capacity):
        super().__init__(registration, max_speed)
        self.fuel_tank_capacity = fuel_tank_capacity

    def print_information(self):
        print(f"Gasoline Car {self.registration}: Max Speed = {self.max_speed} km/h, "
              f"Fuel Tank Capacity = {self.fuel_tank_capacity} L, Odometer = {self.odometer} km")


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.set_speed(150)
gasoline_car.set_speed(120)

electric_car.drive(3)
gasoline_car.drive(3)

electric_car.print_information()
gasoline_car.print_information()
