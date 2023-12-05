"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Abstract vehicle class
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, model: str, colour: str):
        self.__model = model
        self.__colour = colour
        self.__speed = 0
        self.__position = 0

    def set_position(self, new_position: float):
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

    def move(self):
        new_position = self.__position + self.__speed
        self.set_position(new_position)

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def get_icon(self):
        pass

    def get_position_int(self) -> int:
        return int(self.__position)

    def __str__(self) -> str:
        return f"Model: {self.__model}, Colour: {self.__colour}, Speed: {self.__speed}, Position: {self.__position}"

    def __repr__():
        pass
