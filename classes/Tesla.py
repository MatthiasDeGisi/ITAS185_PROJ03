"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Tesla class
"""
import classes.Vehicle as v


class Tesla(v.Vehicle):
    def __init__(self, model: str, colour: str, is_two_motor: bool):
        super().__init__(model, colour)
        self.__is_two_motor = is_two_motor

    @property
    def accel(self) -> float:
        if self.__is_two_motor is True:
            return 0.7
        else:
            return 0.6

    def accelerate(self):
        self.set_speed(self.get_speed() + self.__accel)

    def get_icon(self) -> str:
        return "E"

    def __str__(self) -> str:
        return super().__str__() + f", Two Motor: {self.__is_two_motor}"
