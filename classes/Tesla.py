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
        if self.__is_two_motor is True:
            self.__accel = 0.7
        else:
            self.__accel = 0.6

    def accelerate(self):
        self.set_speed(self.get_speed() + self.__accel)
        super().accelerate()

    def get_icon(self) -> str:
        return "E"

    def __repr__(self) -> str:
        return "Type: Tesla" + super().__repr__() + f", Two Motor: {self.__is_two_motor}"
    
    def __str__(self) -> str:
        if self.__is_two_motor:
            return super().__str__() + " (Two Motor Tesla)"
        else:
            return super().__str__() + " (Tesla)"
