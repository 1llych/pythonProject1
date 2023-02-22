# import random
#
# import random
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.money = 5
#         self.alive = True
#     def to_study(self):
#         print("time to study")
#         self.progress += 0.12
#         self.gladness -=3
#         self.money -=3
#     def to_sleep(self):
#         print("I will sleep")
#         self.gladness +=3
#     def to_chill(self):
#         print("Rest time")
#         self.gladness += 5
#         self.progress - + 0.1
#         self.money -= 3
#     def job(self):
#         print("Time to work")
#         self.gladness -= 5
#         self.progress +=5
#         self.money+=20
#     def is_alive(self):
#         if self.progress < -0.5:
#             print("Cast out...")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depression...")
#             self.alive = False
#         elif self.progress > 5:
#             print("Passed externally...")
#             self.alive = False
#     def end_of_day(self):
#         print(f"Gladness = {self.gladness}")
#         print(f"Progress = {round(self.progress, 2)}")
#         print(f"Money = {self.money}")
#     def live(self, day):
#         day = "Day" + str(day) + "of" + self.name + "life"
#         print(f"{day:=^50}")
#         if self.gladness <= 3 or self.money >= 0 or self.progress >= 1:
#             self.to_chill()
#         elif self.gladness <= 3 or self.money <= 0 or self.progress >=1:
#             self.to_sleep()
#         elif self.gladness > 3 or self.money >= 3:
#             self.to_study()
#         elif self.gladness > 3 or self.money <= 0:
#             self.job()
#
#
#
#         live_cube = random.randint(1, 4)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         elif live_cube == 4:
#             self.job()
#         self.end_of_day()
#
# nick = Student(name="Nick")
# for day in range(365):
#     if nick.alive == False:
#         break
#     nick.live(day)
def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
            result += _
    return result