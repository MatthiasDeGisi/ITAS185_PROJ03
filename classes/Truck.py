"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Truck class
"""
import classes.Vehicle as v


class Truck(v.Vehicle):
    def __init__(self, model: str, colour: str, is_diesel: bool):
        super().__init__(model, colour)
        self.is_diesel = is_diesel

    @property
    def accel(self) -> float:
        if self.is_diesel is True:
            return 0.4
        else:
            return 0.5

    def accelerate(self):
        self.current_speed += self.accel

    def get_icon(self) -> str:
        return "T"

    def __str__(self) -> str:
        return super().str() + f"Diesel: {self.is_diesel}"
