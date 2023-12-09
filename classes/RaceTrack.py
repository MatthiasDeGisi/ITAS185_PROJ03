"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Racetrack class
"""
import os
import time
import classes.Vehicle as v


class RaceTrack:
    def __init__(self, name: str, length: int) -> None:
        """Construct a racetrack object.

        Args:
            name (str): name of the racetrack
            length (int): length of the racetrack
        """
        self.__name = "ITAS Motor Speedway" if not name else name
        self.__length = length + 1
        self.__race_is_won = False

    def get_name(self) -> str:
        """Return the name of the racetrack.

        Returns:
            str: racetrack name
        """
        return self.__name

    def get_length(self) -> int:
        """Return the length of the racetrack

        Returns:
            int: racetrack
        """
        return self.__length

    def print_track(self, race_vehicles: list, round: int) -> None:
        """Print the track with all vehicles on it.

        Args:
            race_vehicles (list): A list of vehicle objects to race
            round (int): the race round
        """
        # initial starting prints, variables
        os.system("cls")
        print(self.get_name())
        print(f"Race Round: [{round}]")
        position_counter = 0
        lane_counter = 1

        # prints the lanes and numbers
        for item in race_vehicles:
            print(f"|{lane_counter}", end="")
            lane_counter += 1
        print("|")

        # prints the rest of track and icons
        for number in range(self.get_length()):
            for item in race_vehicles:
                print("|", end="")
                if item.get_position_int() == position_counter:
                    print(item.get_icon(), end="")
                else:
                    print(" ", end="")
            print(f"|-[Position {position_counter}]")  # line break happens here
            position_counter += 1

        # prints the finish line
        for item in race_vehicles:
            print("=", end="")
            if item.get_position_int() >= self.__length:
                print(item.get_icon(), end="")
            else:
                print("=", end="")
        print("|-[Finish]")

    def get_race_is_won(self) -> bool:
        """Check if the race is won.

        Returns:
            bool: True if a vehicle has crossed the finish line
        """
        return self.__race_is_won

    def set_race_is_won(self, value: bool = True) -> None:
        """Set the race win status.

        Args:
            value (bool, optional): Win status of the race. Defaults to True.
        """
        self.__race_is_won = value

    def print_champions(self, champion: v.Vehicle, runner_up: v.Vehicle) -> None:
        """Print a string with info about the winner and runner up

        Args:
            champion (v.Vehicle): The winner of the race
            runner_up (v.Vehicle): The runner up of the race
        """
        print("Congratulations! The winner is:")
        print(f"{champion}!")
        print("Runner up:")
        print(f"{runner_up}!")

    def find_champions(self, race_vehicles: list) -> list:
        """Find the vehicle that has traveled the farthest (champion) and second farthest (runner up)

        Args:
            race_vehicles (list): list of all vehicle objects in the race

        Returns:
            list: the 2 vehicles that has traveled the farthest
        """
        race_vehicles.sort(reverse=True)
        return [race_vehicles[0], race_vehicles[1]]

    def animation(self) -> None:
        """Print an animation of a car."""
        for frame in self.__animation_list:
            os.system("cls")
            print(frame)
            time.sleep(0.2)
        os.system("cls")
        time.sleep(0.4)
        os.system("cls")

    __animation_list = [
        '''


  
)  _______________  
""))   __   .-""-.""""--._  
      |:.| " ,--. "      _`.
_..--  \/ ( (    ) )--._".-.
_..--------. `--" ;--------"
            `-..-"   
''',
        '''
       __
 _.--""  |
"   |/\| |.--.
_________|  |_)  _______________  
 ___,    "----""))   __   .-""-.""""--._  
|tic|   .---.       |:.| " ,--. "      _`.
|tac|__ \\|// _..--  \/ ( (    ) )--._".-.
_______________..--------. `--" ;--------"
                          `-..-"
''',
        '''
                     __
               _.--""  |
.----.     _.-"   |/\| |.--.
|jrei|__.-"   _________|  |_)  _______________  
|  .-""-.""""" ___,    "----""))   __   .-""-.""""--._  
"-" ,--. "    |tic|   .---.       |:.| " ,--. "      _`.
 ( (    ) ) __|tac|__ \\|// _..--  \/ ( (    ) )--._".-.
  . `--" ;\__________________..--------. `--" ;--------"
   `-..-"                               `-..-"
''',
        '''
                                   __
                             _.--""  |
              .----.     _.-"   |/\| |.--.
              |jrei|__.-"   _________|  |_)  ___________
              |  .-""-.""""" ___,    "----""))   __   .-
              "-" ,--. "    |tic|   .---.       |:.| " ,
               ( (    ) ) __|tac|__ \\|// _..--  \/ ( ( 
                . `--" ;\__________________..--------. `
                 `-..-"                               `-
''',
        '''
                                                 __
                                           _.--""  |
                            .----.     _.-"   |/\| |.--.
                            |jrei|__.-"   _________|  |_
                            |  .-""-.""""" ___,    "----
                            "-" ,--. "    |tic|   .---. 
                             ( (    ) ) __|tac|__ \\|// 
                              . `--" ;\_________________
                               `-..-"                   
''',
    ]
    
    def finish_flag(self) -> None:
        os.system("cls")
        print("""
              ⣀⣠⣤⣔⠒⠀⠉⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⠠⠄⠒⠘⢿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀
⢺⣦⢻⣿⣿⣿⣿⣄⠀⠀⠀⠀⠈⢿⡿⠿⠛⠛⠐⣶⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀
⠈⢿⣧⢻⣿⣿⣿⣿⣆⣀⣠⣴⣶⣿⡄⠀⠀⠀⠀⠘⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⢿⣧⢋⠉⠀⠀⠀⠹⣿⣿⣿⣿⣿⡆⣀⣤⣤⣶⣮⠀⠀⠀⠀⠣⠀⠀⠀⠀
⠀⠀⠈⢿⣧⢂⠀⠀⠀⠀⢘⠟⠛⠉⠁⠀⠹⣿⣿⣿⣿⣷⡀⠀⠀⠀⢣⠀⠀⠀
⠀⠀⠀⠈⢿⣧⢲⣶⣾⣿⣿⣧⡀⠀⠀⠀⢀⣹⠛⠋⠉⠉⠉⢿⣿⣿⣿⣧⠀⠀
⠀⠀⠀⠀⠀⢿⣧⢻⣿⣿⣿⡿⠷⢤⣶⣿⣿⣿⣧⡀⠀⠀⠀⠈⢻⣿⣿⣿⣧⠀
⠀⠀⠀⠀⠀⠈⢿⣧⢛⠉⠁⠀⠀⠀⢻⣿⣿⣿⡿⠗⠒⠒⠈⠉⠉⠉⠙⡉⠛⡃
⠀⠀⠀⠀⠀⠀⠈⢿⣯⢂⠀⠀⠀⡀⠤⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣯⠐⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              """)
        time.sleep(1.5)
