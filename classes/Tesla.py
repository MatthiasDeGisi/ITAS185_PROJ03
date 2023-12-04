"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Tesla class
"""
import classes.Vehicle as v


class Tesla(v.Vehicle):
    def __init__(self, model: str, colour: str, is_two_motor: bool):
        super().__init__(model, colour)
        self.is_two_motor = is_two_motor

    @property
    def accel(self) -> float:
        if self.is_two_motor is True:
            return 0.7
        else:
            return 0.6

    def accelerate(self):
        self.current_speed += self.accel

    def get_icon(self) -> str:
        return "T"

    def __str__(self) -> str:
        return super().str() + f"Diesel: {self.is_diesel}"
