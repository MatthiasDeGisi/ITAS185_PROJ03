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
        """Construct a motorcycle object.

        Args:
            model (str): motorcycle model
            colour (str): motorcycle colour
        """
        super().__init__(model, colour)
        self.__accel = 0.6

    def accelerate(self) -> None:
        """Accelerate the motorcycle based on speed and accel value.
        """
        self.set_speed(self.get_speed() + self.__accel)
        super().accelerate()

    def get_icon(self) -> str:
        """Get the icon for the motorcycle.

        Returns:
            str: motorcycle icon
        """
        return "M"

    def __repr__(self) -> str:
        """Return a string representation of the motorcycle.

        Returns:
            str: a string representation of the motorcycle
        """
        return "Type: Motorcycle," +  super().__repr__()
    
    def __str__(self) -> str:
        """Return a nicely formatted string with motorcycle info.

        Returns:
            str: a nicely formatted string with motorcycle info
        """
        return super().__str__() + " (Motorcycle)"
