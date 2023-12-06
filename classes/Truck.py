"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Truck class
"""
import classes.Vehicle as v


class Truck(v.Vehicle):
    def __init__(self, model: str, colour: str, is_diesel: bool):
        super().__init__(model, colour)
        self.__is_diesel = eval(is_diesel)
        if self.__is_diesel is True:
            self.__accel = 0.4
        else:
            self.__accel = 0.5

    def accelerate(self):
        self.set_speed(self.get_speed() + self.__accel)

    def get_icon(self) -> str:
        return "T"

    def __str__(self) -> str:
        return super().__str__() + f", Diesel: {self.__is_diesel}"
