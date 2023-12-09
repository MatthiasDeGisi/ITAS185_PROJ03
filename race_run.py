"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: File that runs the race
"""
import classes.Motorcycle as m
import classes.Truck as t
import classes.Tesla as e
import classes.RaceTrack as r

import os
import time

if __name__ == "__main__":
    os.system("cls")
    print("Welcome to racepy!")

    # user input (validated) loop
    track_name = input("Enter a name for your racetrack (or leave blank for default): ")
    while True:
        try:
            track_length = int(input("Enter a track length (integer from 20-40): "))
            assert track_length >= 20, "Track length cannot be lower than 20"
            assert track_length <= 40, "Track length cannot be higher than 40"
        except ValueError:
            print("Track length must be an integer")
        except AssertionError as msg:
            print(msg)
        else:
            # creates the racetrack
            racetrack = r.RaceTrack(track_name, track_length)
            break

    # main loop to get vehicle file and run race
    while True:
        racetrack.animation()
        race_vehicles = []
        # user input
        file_name = input("Enter the name of a text data file to open: ")
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        # opening and processing lines
        try:
            with open(file_name) as file_handle:
                file_contents = file_handle.readlines()

        except FileNotFoundError as msg:
            print(msg)
            time.sleep(1)
            continue

        # create list of vehicle objects
        else:
            for item in file_contents:
                line = item.strip("\n ,").split(",")
                if line[0] == "Motorcycle":
                    race_vehicles.append(m.Motorcycle(line[1], line[2]))
                elif line[0] == "Truck":
                    race_vehicles.append(t.Truck(line[1], line[2], line[3]))
                elif line[0] == "Tesla":
                    race_vehicles.append(e.Tesla(line[1], line[2], line[3]))

        # starts race
        round = 0
        racetrack.print_track(race_vehicles, round)
        while not racetrack.get_race_is_won():
            round += 1
            for item in race_vehicles:
                item.accelerate()
                item.move()
                if item.get_position_int() > racetrack.get_length():
                    racetrack.set_race_is_won()
            racetrack.print_track(race_vehicles, round)
            time.sleep(1)

        # determines winner
        racetrack.finish_flag()
        racetrack.print_track(race_vehicles, round)
        champions = racetrack.find_champions(race_vehicles)
        racetrack.print_champions(*champions)

        # play again or exit
        try:
            input("Press enter to race again, or ctrl + c to exit.")
            racetrack.set_race_is_won(False)
            continue

        except KeyboardInterrupt:
            racetrack.animation()
            print("Thanks for playing racepy!")
            time.sleep(1)
            break
