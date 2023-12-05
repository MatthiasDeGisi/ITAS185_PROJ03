"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Motorcycle class
"""
import classes.Vehicle as v


class Motorcycle(v.Vehicle):
    def __init__(
        self,
        model,
        colour,
    ):
        super().__init__(model, colour)

    @property
    def accel(self) -> float:
        return 0.6

    def accelerate(self):
        self.set_speed(self.get_speed() + self.__accel)

    def get_icon(self) -> str:
        return "M"

    def __str__(self) -> str:
        return super().__str__()
