# Trollventure 1 - Fight trolls and rescue the princess! ;)
# Base Code: Roman Friske
# Battle System / Integration: Alexander Schulze

import random
from battle_system import battle

### Variables/Lists ###
    
list = [
        # room 1
        {"west": 2, "east": 5},
        # room 2
        {"east": 1, "north": 3},
        # room 3
        {"south": 2, "east": 4},
        # room 4
        {"west": 3, "north": 8, "east": 6},
        # room 5
        {"west": 1},
        # room 6
        {"west": 4, "north": 7},
        # room 7
        {"south": 6, "west": 8},
        # room 8
        {"west": 9, "south": 4, "east": 7},
        # room 9
        {"east": 8}
        ]

random_battle = 0
princess = 9
pos = 1
room = list[pos-1]

########################## Main Code ############################

while (pos != princess):
    print(f"You are in room {pos}. No princess found.")
    heading = input("Where do you want to go to? east, west, north, south: ")
    
    if (heading in room):
        pos = room[heading]
        room = list[pos-1] 
        random_battle = random.randint(1,12)
        if random_battle > 9:
            battle()
    else:
        print("You can't move to ", heading)
print(f"You are in room {pos}. You have found the princess!")