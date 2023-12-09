"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Tesla class
"""
import classes.Vehicle as v


class Tesla(v.Vehicle):
    def __init__(self, model: str, colour: str, is_two_motor: bool):
        """Construct a Tesla object.

        Args:
            model (str): model of the
            colour (str): _description_
            is_two_motor (bool): _description_
        """
        super().__init__(model, colour)
        self.__is_two_motor = eval(is_two_motor)
        self.__accel = 0.7 if self.__is_two_motor else 0.6

    def accelerate(self):
        """Accelerate the Tesla."""
        self.set_speed(self.get_speed() + self.__accel)
        super().accelerate()

    def get_icon(self) -> str:
        """Return the "E" Tesla icon.

        Returns:
            str: the "E" Tesla icon
        """
        return "E"

    def __repr__(self) -> str:
        """Return a representation of the Tesla and its attributes.

        Returns:
            str: a representation of the Tesla
        """
        return (
            "Type: Tesla, " + super().__repr__() + f", Two Motor: {self.__is_two_motor}"
        )

    def __str__(self) -> str:
        """Return a nicely formatted string with info about the
        Tesla (Type, model, colour, position, speed, two motor).

        Returns:
            str: a nicely formatted string with info about the Tesla
        """
        type = "Two Motor Tesla" if self.__is_two_motor else "Tesla"
        return super().__str__() + f" ({type})"
