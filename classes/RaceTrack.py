"""
Course: ITAS 185 - Introduction to Programming
Project 03
Description: Racetrack class
"""
import os
import time
import classes.Vehicle as v


class RaceTrack:
    def __init__(self, name: str = "ITAS Motor Speedway", length: int = 20) -> None:
        self.__name = name
        self.__length = length
        self.__race_is_won = False

    def get_name(self) -> str:
        return self.__name

    def get_length(self) -> int:
        return self.__length

    def print_track(self, race_vehicles: list, round: int) -> None:
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
        time.sleep(1)

    def get_race_is_won(self) -> bool:
        return self.__race_is_won

    def set_race_is_won(self, value: bool = True) -> None:
        self.__race_is_won = value

    def champion(self, champion: v.Vehicle) -> None:
        print("Congratulations! The winner is:")
        print(champion)

    def find_champion(self, race_vehicles: list) -> v.Vehicle:
        race_vehicles.sort(reverse=True)
        return race_vehicles[0]

    def animation(self) -> None:
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
