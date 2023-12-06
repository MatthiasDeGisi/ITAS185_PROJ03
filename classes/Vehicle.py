"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Abstract vehicle class
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, model: str, colour: str) -> None:
        self.__model = model
        self.__colour = colour
        self.__speed = 0
        self.__position = 0

    def set_position(self, new_position: float) -> None:
        self.__position = new_position

    def set_speed(self, speed: float) -> float:
        self.__speed = speed

    def get_model(self) -> str:
        return self.__model

    def get_colour(self) -> str:
        return self.__colour

    def get_speed(self) -> float:
        return self.__speed

    def get_position(self) -> float:
        return self.__position

    def get_position_int(self) -> int:
        return int(self.__position)
    
    def move(self) -> None:
        new_position = self.get_position() + self.get_speed()
        self.set_position(new_position)

    @abstractmethod
    def accelerate(self) -> None:
        pass

    @abstractmethod
    def get_icon(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Model: {self.get_model()}, Colour: {self.get_colour()}, Speed: {self.get_speed():.2f}, Position: {self.get_position():.2f}"

    def __eq__(self, other: "Vehicle"):
        return self.get_position() == other.get_position()
    
    def __lt__(self, other: "Vehicle"):
        return self.get_position() < other.get_position()