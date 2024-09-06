class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return ("Car Details:\n"
                f"Registration number:{self.registration_number}\n"
                f"Maximum Speed:{self.max_speed}\n"
                f"Current Speed:{self.current_speed}\n"
                f"Travelled Distance:{self.travelled_distance}")


number = input("enter the registration number of the car")
max_speed = input("enter the max speed of the car")
car = Car(number, max_speed)
print(car)