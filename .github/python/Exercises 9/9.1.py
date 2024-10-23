import random


class Car:
    def __init__(self, registration_number, max_speed, hour):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.hour = hour

    def accelerate(self, accelerate_speed):
        new_speed = self.current_speed + accelerate_speed
        if 0 < new_speed <= self.max_speed:
            self.current_speed = new_speed
        elif new_speed <= 0:
            self.current_speed = 0
        elif new_speed >= self.max_speed:
            self.current_speed = self.max_speed

    def drive(self):
        self.travelled_distance += self.current_speed * self.hour

    def __str__(self):
        return ("Car Details:\n"
                f"Registration number:{self.registration_number}\n"
                f"Maximum Speed:{self.max_speed}\n"
                f"Current Speed:{self.current_speed}\n"
                f"Travelled Distance:{self.travelled_distance}\n"
                f"Travelled Time:{self.hour} hours")


cars = []
for i in range(10):
    registration_number = f"ABC_{i + 1}"
    max_speed = random.randint(100, 200)
    new_car = Car(registration_number, max_speed,0)
    cars.append(new_car)
hour = 0
race_finished = False

while not race_finished:
    for car in cars:
        car.hour += 1
        accelerate = random.randint(-10, 15)
        car.drive()
        car.accelerate(accelerate)

        if car.travelled_distance >= 10000:
            race_finished = True
for car in cars:
    print(car)
