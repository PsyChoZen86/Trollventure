def battle ():
    #A simple test for a round based battle system with randomly generated damage
    #and remaining enemy hit points display.
    #Future versions should include: player hp display - enemy attacking back - more battle options
    #Alexander Schulze 22.11.2018

    #module needed for random damage calculation
    import random

    enemy_hp = 50 #indicator for remaining enemy hitpoints
    hp_symbol = "x" #symbol used for visualisation
    battle_active = True #indicator for battle loop (while battle is active)
    player_choice = "o" #placeholder for player choice variable
    attack_power = 0 #stores the last attacks value

    #returns number of remaining HP as symbols to visualize it
    def hp_graphic(hp, sym):
        return hp * sym
    #returns a string to print out the possible choices
    def choose():
        return ("""
        (a)ttack
        (r)un

    Choose your destiny: """)

    ########## main code ##########
    print ("\n!!!! Enemy appeared. !!!!")
    input("(hit enter to proceed)")

    while battle_active == True and enemy_hp > 0:
        #display remaining enemy hp
        print ("\nTroll HP:", enemy_hp) 
        print (hp_graphic(enemy_hp, hp_symbol))
        
        #ask for player choice
        player_choice = input (choose())
        
        #attack -> calculate and print damage
        if player_choice == "a":
            attack_power = random.randint(8,18)
            print ("\nYou did", attack_power, "damage.")
            enemy_hp = enemy_hp - attack_power
        #run -> print escape message & leave loop    
        elif player_choice == "r":
            print ("You ran away...")
            battle_active = False
        #other command -> print error message & nothing more
        else:
            print ("\nPlease try again!\n")
        
    print ("The battle is over!\n")
    
battle()

