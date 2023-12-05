"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: File that runs the race
"""
import classes.Motorcycle as m
import classes.Truck
import classes.Tesla
import classes.RaceTrack

if __name__ == "__main__":
    while True:
        race_vehicles = []
        file_name = input(
            "Enter the name of a text data file to open: "
        )
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        
        try:
            with open(file_name) as file_handle:
                counter = 0
                for line in file_name:
                    file = file_handle.readline()
                    # print(file)
                    race_vehicles.append(m.Motorcycle("Kawasaki", "green"))
                    print(race_vehicles[0])
                    counter += 1
                
        except FileNotFoundError as msg:
            print(msg)
            continue
            
        
        break