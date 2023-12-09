"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Truck class
"""
import classes.Vehicle as v


class Truck(v.Vehicle):
    def __init__(self, model: str, colour: str, is_diesel: bool) -> None:
        """Construct a Truck object.

        Args:
            model (str): The model of the truck
            colour (str): The colour of the truck
            is_diesel (bool): True if the truck is diesel, else false
        """
        super().__init__(model, colour)
        self.__is_diesel = eval(is_diesel)
        self.__accel = 0.4 if self.__is_diesel else 0.5

    def accelerate(self) -> None:
        """Accelerate the truck."""
        self.set_speed(self.get_speed() + self.__accel)
        super().accelerate()

    def get_icon(self) -> str:
        """Get the "T" truck icon.

        Returns:
            str: The truck icon "T"
        """
        return "T"

    def __repr__(self) -> str:
        """Return a representation of the truck object and its attributes.

        Returns:
            str: A representation of the truck object
        """
        return "Type: Truck, " + super().__repr__() + f", Diesel: {self.__is_diesel}"

    def __str__(self) -> str:
        """Return a nicely formatted string with info about
        the truck (Diesel, colour, model, speed, position).

        Returns:
            str: a nicely formatted string with info about the truck.
        """
        type = "Diesel Truck" if self.__is_diesel else "Truck"
        return super().__str__() + f" ({type})"
