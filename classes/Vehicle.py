"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Abstract vehicle class
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, model: str, colour: str):
        self.model = model
        self.colour = colour
        self.speed = 0
        self.position = 0

    def set_position(self, new_position: float):
        self.position = new_position

    def set_speed(self, speed: float) -> float:
        self.speed = speed

    def get_model(self) -> str:
        return self.model

    def get_colour(self) -> str:
        return self.colour

    def get_speed(self) -> float:
        return self.speed

    def get_position(self) -> float:
        return self.position

    def move(self):
        new_position = self.position + self.speed
        self.set_position(new_position)

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def get_icon(self):
        pass

    def get_position_int(self) -> int:
        return int(self.position)

    def __str__(self) -> str:
        return f"Model: {self.model}, Colour: {self.colour}, Speed: {self.speed}, Position: {self.position}"

    def __repr__():
        pass
