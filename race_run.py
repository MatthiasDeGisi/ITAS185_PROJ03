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
    while True:
        race_vehicles = []
        os.system("cls")

        # user input
        file_name = input("Enter the name of a text data file to open: ")
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        # opening and processing lines
        try:
            with open(file_name) as file_handle:
                for line in file_handle:
                    read_attributes = line.split(",")

                    # removes the \n
                    del read_attributes[-1]

                    # instantiates object based on first field
                    if read_attributes[0] == "Motorcycle":
                        race_vehicles.append(
                            m.Motorcycle(read_attributes[1], read_attributes[2])
                        )
                    elif read_attributes[0] == "Truck":
                        race_vehicles.append(
                            t.Truck(
                                read_attributes[1],
                                read_attributes[2],
                                read_attributes[3],
                            )
                        )
                    elif read_attributes[0] == "Tesla":
                        race_vehicles.append(
                            e.Tesla(
                                read_attributes[1],
                                read_attributes[2],
                                read_attributes[3],
                            )
                        )

        except FileNotFoundError as msg:
            print(msg)
            continue

        # instantiate racetrack
        racetrack = r.RaceTrack()
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

        # determines winner
        champion = racetrack.find_champion(race_vehicles)
        racetrack.champion(champion)

        # play again or exit
        try:
            input("Press enter to race again, or ctrl + c to exit.")
            continue
        except KeyboardInterrupt:
            os.system("cls")
            print("Thanks for playing!")
            time.sleep(1)
            break
