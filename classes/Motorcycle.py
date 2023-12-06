"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Motorcycle class
"""
import classes.Vehicle as v


class Motorcycle(v.Vehicle):
    def __init__(
        self,
        model: str,
        colour: str,
    ) -> None:
        super().__init__(model, colour)
        self.__accel = 0.6

    def accelerate(self) -> None:
        self.set_speed(self.get_speed() + self.__accel)
        super().accelerate()

    def get_icon(self) -> str:
        return "M"

    def __str__(self) -> str:
        return super().__str__()
