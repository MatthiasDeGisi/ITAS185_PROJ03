"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Racetrack class
"""
import os
import time


class RaceTrack:
    def __init__(self, name="ITAS Motor Speedway", length=20):
        self.__name = name
        self.__length = length
        self.__round = 0

    def get_name(self) -> str:
        return self.__name

    def get_length(self) -> int:
        return self.__length

    def print_track(self, race_list: list, round: int):
        os.system("cls")
        print(f"Race Round: [{round}]")
        position_counter = 0
        lane_counter = 1
        for item in race_list:
            print(f"|{lane_counter}", end="")
            lane_counter += 1
        print("|")
        for number in range(self.__length):
            for item in race_list:
                print("|", end="")
                if item.get_position_int() == position_counter:
                    print(item.get_icon(), end="")
                else:
                    print(" ", end="")
            print(f"|-[Position {position_counter}]")
            position_counter += 1
        for item in race_list:
            print("=", end="")
            if item.get_position_int() == self.__length + 1:
                print(item.get_icon(), end="")
            else:
                print("=", end="")
        print("|-[Finish]")
        time.sleep(2)

    def champion(self, winner):
        print("Congratulations! The winner is:")
        print(winner)
