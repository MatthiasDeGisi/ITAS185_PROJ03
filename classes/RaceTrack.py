"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Racetrack class
"""
import os


class RaceTrack:
    def __init__(self, name: str, length: int):
        self.__name = name
        self.__length = length
        self.__round = 0

    def get_name(self) -> str:
        return self.__name

    def get_length(self) -> int:
        return self.__length

    def __str__(self, race_list) -> str:
        print(f"Race Round: [{self.get_round()}]")
        counter = 0
        for number in range(self.__length):
            print("|")
            for item in race_list:
                if item.get_position_int() == counter:
                    print(item.get_icon())
                else:
                    print(" ")

    def champion(self, winner):
        print("Congratulations! The winner is:")
        print(winner)

    def reset_round(self):
        self.__round = 0

    def get_round(self):
        return self.__round
