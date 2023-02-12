import random

import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.fatigue = 0
        self.alive = True
    def to_hunting(self):
        print("time to hunting")
        self.fatigue += 0.12
        self.satiety -=3
    def to_sleep(self):
        print("I will sleep")
        self.satiety +=3
    def to_chill(self):
        print("Rest time")
        self.satiety += 5
        self.fatigue - + 0.1
    def is_alive(self):
        if self.fatigue < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.satiety <= 0:
            print("Depression...")
            self.alive = False
        elif self.fatigue > 5:
            print("Passed externally...")
            self.alive = False
    def end_of_day(self):
        print(f"Satiety = {self.satiety}")
        print(f"Fatigue = {round(self.fatigue, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()


nyavchyk = (name="nyavchyk")
for day in range(365):
    if nyavchyk.alive == False:
        break
    nyavchyk.live(day)