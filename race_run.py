"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: File that runs the race
"""
import classes.Motorcycle as m #test
import classes.Truck as t
import classes.Tesla as e
import classes.RaceTrack as r

if __name__ == "__main__":
    while True:
        race_vehicles = []
        file_name = input("Enter the name of a text data file to open: ")
        if not file_name.endswith(".txt"):
            file_name += ".txt"

        try:
            with open(file_name) as file_handle:
                for line in file_handle:
                    read_attributes = line.split(",")
                    del read_attributes[-1]
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

        print(race_vehicles[0])
        break
