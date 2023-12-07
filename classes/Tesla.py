"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Tesla class
"""
import classes.Vehicle as v


class Tesla(v.Vehicle):
    def __init__(self, model: str, colour: str, is_two_motor: bool):
        super().__init__(model, colour)
        self.__is_two_motor = eval(is_two_motor)
        self.__accel = 0.7 if self.__is_two_motor is True else 0.6

    def accelerate(self):
        self.set_speed(self.get_speed() + self.__accel)
        super().accelerate()

    def get_icon(self) -> str:
        return "E"

    def __repr__(self) -> str:
        return "Type: Tesla" + super().__repr__() + f", Two Motor: {self.__is_two_motor}"
    
    def __str__(self) -> str:
        type = "Two Motor Tesla" if self.__is_two_motor else "Tesla"
        return super().__str__() + f" ({type})"

