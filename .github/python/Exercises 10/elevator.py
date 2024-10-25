class elevator:
    def __init__(self, bottom_floor, top_floor,elevator_id):
        self.elevator_id= elevator_id
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator {self.elevator_id} at {self.current_floor} floor")
        else:
            print(f"Elevator {self.elevator_id} is at the top floor")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator {self.elevator_id} at {self.current_floor} floor")
        else:
            print(f"Elevator {self.elevator_id} is at the bottom floor")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("error floor ")
            return
        while target_floor > self.current_floor:
            self.floor_up()
        while target_floor < self.current_floor:
            self.floor_down()


class building:
    def __init__(self, bottom_floor, top_floor, number):
        self.bottom_floor = bottom_floor
        self.elevators = [elevator(bottom_floor, top_floor, i + 1) for i in range(number)]

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 0 or elevator_number > len(self.elevators):
            print("error")
            return
        print(f"Elevator {elevator_number}  to {target_floor} floor ")
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("Fire alarm! All elevators are moving to the bottom floor.")
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"Running elevator {i} to the bottom floor:")
            elevator.go_to_floor(self.bottom_floor)


building = building(0, 10, 3)
building.run_elevator(2, 3)
building.fire_alarm()
building.run_elevator(2, 5)