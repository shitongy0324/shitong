import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


    def accelerate(self, accelerate_speed):
        new_speed = self.current_speed + accelerate_speed
        if 0 < new_speed <= self.max_speed:
            self.current_speed = new_speed
        elif new_speed <= 0:
            self.current_speed = 0
        elif new_speed >= self.max_speed:
            self.current_speed = self.max_speed

    def drive(self,hour):
        self.travelled_distance += self.current_speed * hour


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_pass(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration':<15}{'Max Speed':<12}{'Current Speed':<15}{'Travelled Distance':<20}")
        for car in self.cars:
            print(
                f"{car.registration_number:<15}{car.max_speed:<12}{car.current_speed:<15}{car.travelled_distance:<20}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


cars = [Car(f"ABC-{i:03}", random.randint(100, 200)) for i in range(10)]
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_pass()
    hours += 1
    if hours % 10 == 0:
        print(f"\nStatus after {hours} hours:")
        race.print_status()

print(f"\nFinal status after {hours} hours:")
race.print_status()
