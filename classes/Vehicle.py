"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Abstract vehicle class
"""
from abc import ABC, abstractmethod
import random


class Vehicle(ABC):
    def __init__(self, model: str, colour: str) -> None:
        """Construct a vehicle object.

        Args:
            model (str): model of the vehicle
            colour (str): colour of the vehicle
        """
        self.__model = model
        self.__colour = colour
        self.__speed = 0.0
        self.__position = 0.0
        self.__acceleration_change = [-0.2, -0.1, 0, 0.1, 0.2]
        self.__weight_values = (1, 2, 6, 2, 1)

    def set_position(self, new_position: float) -> None:
        """Set the position of the vehicle.

        Args:
            new_position (float): new position for the vehicle
        """
        self.__position = new_position

    def set_speed(self, speed: float) -> None:
        """Set the speed of the vehicle.

        Args:
            speed (float): the speed to be set
        """
        self.__speed = speed

    def get_model(self) -> str:
        """Get the model of the vehicle.

        Returns:
            str: model of the vehicle
        """
        return self.__model

    def get_colour(self) -> str:
        """Get the colour of the vehicle.

        Returns:
            str: colour of the vehicle
        """
        return self.__colour

    def get_speed(self) -> float:
        """Get the speed of the vehicle.

        Returns:
            float: speed of the vehicle
        """
        return self.__speed

    def get_position(self) -> float:
        """Get the position of the vehicle.

        Returns:
            float: position of the vehicle
        """
        return self.__position

    def get_position_int(self) -> int:
        """Get an integer position of the vehicle.

        Returns:
            int: integer position of the vehicle
        """
        return int(self.__position)

    def move(self) -> None:
        """Move the vehicle based on speed and position."""
        new_position = self.get_position() + self.get_speed()
        self.set_position(new_position)

    def accelerate(self) -> None:
        """Accelerate the vehicle based on speed and a random number."""
        variance = random.choices(
            self.__acceleration_change, weights=self.__weight_values
        )
        variance = variance[0]
        self.set_speed(self.get_speed() + variance)

    @abstractmethod
    def get_icon(self) -> None:
        """Abstract method to get the vehicle icon."""
        pass

    def __repr__(self) -> str:  # Should add accel to this
        """Return a representation of the vehicle.

        Returns:
            str: representation of the vehicle
        """
        return f"Model: {self.get_model()}, Colour: {self.get_colour()}, Speed: {self.get_speed():.2f}, Position: {self.get_position():.2f}"

    def __lt__(self, other: "Vehicle") -> bool:
        """Determine whether a vehicle is less than another based on position

        Args:
            other (Vehicle): another vehicle

        Returns:
            bool: True if self is behind other
        """
        return self.get_position() < other.get_position()

    def __str__(self) -> str:
        """Return a nicely formatted string about the vehicle

        Returns:
            str: a nicely formatted string about the vehicle
        """
        return self.get_colour() + " " + self.get_model()
