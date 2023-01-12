warrior = False
mage = False
rogue = False

Class = None

abilityMax = 0

playerHealth = 100
playerMax = 100

enemy = None
enemyHealth = 0
enemyMax = 0
enemyStats = 0
enemyLevel = 0

uses = 3
usesMax = 3

damage = 0
bloodlust = 0
damageUp = 0 + bloodlust
frozen = False


level = 1
exp = 0
maxexp = 100
coins = 0
pots = 0
gpots = 0

Forest = False
Swamps = False
Volcano = False
Dungeon = False



# The save

gameState = {
    "warrior": False,
    "mage": False,
    "rogue": False,
    "Class": None,
    "abilityMax": 0,
    "playerHealth": 100,
    "playerMax": 100,
    "damage": 0,
    "damageUp": 0,
    "level": 1,
    "exp": 0,
    "maxexp": 100,
    "coins": 0,
    "pots": 0,
    "gpots": 0,
    "uses": 3,
}



# Important imports

import pickle
import time
import os
import random

#Slowprint function

def slowprint(text, delay = 0.01): 
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    print("\x1B[2J\x1B[1;1H") #Control character
        
        
    
def updateGameState():
    # Update the gameState dictionary with the current values of the game's variables
    gameState["playerHealth"] = playerHealth
    gameState["playerMax"] = playerMax
    gameState["coins"] = coins
    gameState["level"] = level
    gameState["pots"] = pots
    gameState["gpots"] = gpots
    gameState["damageUp"] = damageUp
    gameState["exp"] = exp
    gameState["maxexp"] = maxexp
    gameState["Class"] = Class
    gameState["abilityMax"] = abilityMax
    gameState["warrior"] = warrior
    gameState["mage"] = mage
    gameState["rogue"] = rogue
    gameState["uses"] = uses
    gameState["usesMax"] = usesMax

    # Save the updated gameState dictionary to a file using pickle
    with open("saved_game.pickle", "wb") as f:
        pickle.dump(gameState, f)
    menu()
    
    

def save():
    updateGameState()
    
    
def reset():
    global warrior
    global mage 
    global rogue
    global Class
    global abilityMax
    global playerHealth
    global playerMax
    global enemy
    global enemyHealth
    global enemyMax
    global enemyStats
    global damage
    global damageUp
    global level 
    global exp
    global maxexp
    global coins
    global pots
    global gpots
    global Forest
    global Swamps
    global Volcano
    global Dungeon
    global uses
    global usesMax
    warrior = False
    mage = False
    rogue = False
    Class = None
    abilityMax = 0
    playerHealth = 100
    playerMax = 100
    enemy = None
    enemyHealth = 0
    enemyMax = 0
    enemyStats = 0
    damage = 0
    damageUp = 0
    level = 1
    exp = 0
    maxexp = 100
    coins = 0
    pots = 0
    gpots = 0
    Forest = False
    Swamps = False
    Volcano = False
    Dungeon = False
    uses = 3
    usesMax = 3
    gameState = {
        "warrior": False,
        "mage": False,
        "rogue": False,
        "Class": None,
        "playerHealth": 100,
        "playerMax": 100,
        "damage": 0,
        "damageUp": 0,
        "level": 1,
        "exp": 0,
        "maxexp": 100,
        "coins": 0,
        "pots": 0,
        "gpots": 0,
        "uses": 3,
        "usesMax": 3,
    }

    # Save the reset gameState dictionary to a file using pickle
    with open("saved_game.pickle", "wb") as f:
        pickle.dump(gameState, f)
    quit()
    
    

def load_game():
    global playerHealth
    global playerMax
    global coins
    global level
    global pots
    global gpots
    global damageUp
    global exp
    global maxexp
    global Class
    global abilityMax
    global warrior
    global mage
    global rogue
    global uses
    global usesMax
    
    # Load the gameState dictionary from a file using pickle
    with open("saved_game.pickle", "rb") as f:
        gameState = pickle.load(f)

    # Update the game's variables with the values from the gameState dictionary
    playerHealth = gameState["playerHealth"]
    playerMax = gameState["playerMax"]
    coins = gameState["coins"]
    level = gameState["level"]
    pots = gameState["pots"]
    gpots = gameState["gpots"]
    damageUp = gameState["damageUp"]
    exp = gameState["exp"]
    maxexp = gameState["maxexp"]
    Class = gameState["Class"]
    abilityMax = gameState["abilityMax"]
    warrior = gameState["warrior"]
    mage = gameState["mage"]
    rogue = gameState["rogue"]
    uses = gameState["uses"]
    usesMax = gameState["usesMax"]

    # Print the loaded dictionary to verify that it was loaded correctly
    print(gameState)
    menu()
    


#SaveResetLoad, here is where you can save, reset old data or load up saved data
    
def saveResetLoad():
    os.system('cls')
    # Show the menu options
    print("| Save (1) | Reset (2) | Load (3) | Go back (0) |")
    slowprint("What do you want to do? ")
    choice = input("")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        os.system('cls')
        save()
    
    elif choice == "2":
        os.system('cls')
        reset()

    elif choice == "3":
        os.system('cls')
        load_game()
        
    elif choice =="0":
        os.system('cls')
        menu()
        
    else:
        os.system('cls')
        slowprint("Invalid choice.")
        slowprint("Press enter to continue.")
        input("")
        menu()
        
        
        
# The fountain is where you reset your ability charges and upgrade your ability charge amount
    
def fountain():
    global coins
    global uses
    global usesMax
    
    os.system('cls')
    slowprint("Welcome to the fountain!")
    slowprint("| Refresh ability uses, Costs 3 coins (1) | Upgrade ability uses, Costs 7 coins (2) | Go back (0) |")
    slowprint("What do you want to do?")
    choice = input("")
    if choice == "1":
        if coins >= 3:
            coins = coins - 3
            if uses < usesMax:
                uses = usesMax
                os.system('cls')
                slowprint("Your uses have been refilled!")
                slowprint("It cost 3 coins.")
                slowprint("Press enter to continue")
                input("")
                fountain()
            else:
                os.system('cls')
                slowprint("You already have max uses.")
                slowprint("Press enter to continue")
                input("")
                fountain()
                
        else:
            os.system('cls')
            slowprint("You dont have enough coins.")
            slowprint("Press enter to continue")
            input("")
            fountain()
            
    elif choice == "2":
        if coins >= 7:
            coins = coins - 7
            usesMax = usesMax + 1
            uses = usesMax
            os.system('cls')
            slowprint("Your ability uses have been upgraded")
            slowprint("It cost 7 coins.")
            slowprint("Press enter to continue")
            input("")
            fountain()
            
        else:
            os.system('cls')
            slowprint("You dont have enough coins.")
            slowprint("Press enter to continue")
            input("")
            fountain()
            
    elif choice == "0":
        menu()
        
        
        
def Bloodlust():
    global bloodlust
    global damageUp
    global damage
    
    damage = 5 + damageUp
    bloodlust += damage
    slowprint(f"You cast bloodlust, boosting your damage by {damage} temporarily.")
    slowprint("Press enter to continue")
    input("")
    damage = damage - damage
    calculateBloodlust()
        
def calculateBloodlust():
    global bloodlust
    global damageUp
    damageUp = damageUp + bloodlust
    slowprint(f"Your health: {playerHealth}/{playerMax} | Level: {enemyLevel} {enemy}s health: {enemyHealth}/{enemyMax}")
    slowprint("Press enter to continue")
    input("")
    if playerHealth <= 0:
         slowprint("You took too much damage and died.")
         quit()
    else:
        postFight()

# MageFightAbilities is called upon when using mage abilities in combat. 

def warriorFightAbilities():
    global playerHealth
    global playerMax
    global enemyHealth
    global enemyMax
    global enemyStats
    global damage
    global damageUp
    global pots
    global gpots
    global coins
    global exp
    global maxexp
    global level
    global enemy
    global enemyLevel
    global uses
    global bloodlust
    
    os.system('cls')
    slowprint(f"Ability uses: {uses}")
    slowprint("| Shield slam, Cost 1 (1) | Cleave, Cost 2 (2) | Bloodlust, Cost 3 (3) | Go back (0)")
    slowprint("What do you do?")
    choice = input("")
    if choice == "1":
        if uses >= 1:
            os.system('cls')
            uses = uses - 1
            damage = damage + (8 + damageUp)
            slowprint(f"You cast shield slam knocking the {enemy} with your shield, dealing {damage} damage and gaining {damage} health.")
            slowprint("Press enter to continue")
            input("")
            enemyHealth = enemyHealth - damage
            playerHealth = playerHealth + damage 
            if playerHealth > playerMax:
                playerHealth = playerMax
            damage = damage - damage
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            warriorFightAbilities()
            
    if choice == "2":
        if uses >= 2:
            os.system('cls')
            uses = uses - 2
            damage = damage + (5 + damageUp) + (enemyHealth // 7)   
            slowprint(f"You cleave the {enemy}, dealing {damage} damage to it.")
            slowprint("Press enter to continue")
            input("")
            enemyHealth = enemyHealth - damage
            damage = damage - damage
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            warriorFightAbilities()
            
    if choice == "3":
        if uses >= 3:
            os.system('cls')
            uses = uses - 3
            Bloodlust()
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            warriorFightAbilities()
    
    elif choice == "0":
        fight()
            
    slowprint(f"Your health: {playerHealth}/{playerMax} | Level: {enemyLevel} {enemy}s health: {enemyHealth}/{enemyMax}")
    slowprint("Press enter to continue")
    damage = damage - damage
    input("")
    if playerHealth <= 0:
         slowprint("You took too much damage and died.")
         quit()
    else:
        postFight()
    


# MageFightAbilities is called upon when using mage abilities in combat. 
    
def mageFightAbilities():
    global playerHealth
    global playerMax
    global enemyHealth
    global enemyMax
    global enemyStats
    global damage
    global damageUp
    global pots
    global gpots
    global coins
    global exp
    global maxexp
    global level
    global enemy
    global enemyLevel
    global uses
    global frozen
    
    os.system('cls')
    slowprint(f"Ability uses: {uses}")
    slowprint("| Fireball, Cost 1 (1) | Frostbolt, Cost 2 (2) | Song of fire & ice, Cost 3 (3) | Go back (0)")
    slowprint("What do you do?")
    choice = input("")
    if choice == "1":
        if uses >= 1:
            os.system('cls')
            uses = uses - 1
            damage = damage + (7 + damageUp)
            slowprint(f"You cast a fireball at the {enemy}, dealing {damage} damage.")
            slowprint("Press enter to continue")
            input("")
            enemyHealth = enemyHealth - damage
            damage = damage - damage
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            mageFightAbilities()
            
    if choice == "2":
        if uses >= 2:
            os.system('cls')
            uses = uses - 2
            frozen = True
            damage = damage + (5 + damageUp)
            slowprint(f"You cast a frostbolt at the {enemy}, freezing it and dealing {damage} damage.")
            slowprint("Press enter to continue")
            input("")
            enemyHealth = enemyHealth - damage
            damage = damage - damage
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            mageFightAbilities()
            
    if choice == "3":
        if uses >= 3:
            os.system('cls')
            uses = uses - 3
            frozen = True
            damage = damage + (13 + damageUp)
            slowprint(f"You sing the song of fire & ice, freezing the {enemy} and dealing {damage} damage to it.")
            slowprint("Press enter to continue")
            input("")
            enemyHealth = enemyHealth - damage
            damage = damage - damage
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            mageFightAbilities()
    
    elif choice == "0":
        fight()
            
    slowprint(f"Your health: {playerHealth}/{playerMax} | Level: {enemyLevel} {enemy}s health: {enemyHealth}/{enemyMax}")
    slowprint("Press enter to continue")
    damage = damage - damage
    input("")
    if playerHealth <= 0:
         slowprint("You took too much damage and died.")
         quit()
    else:
        postFight()
            
    
    


# RogueFightAbilities is called upon when using rogue abilities in combat. 

def rogueFightAbilities():
    global playerHealth
    global playerMax
    global enemyHealth
    global enemyMax
    global enemyStats
    global damage
    global damageUp
    global pots
    global gpots
    global coins
    global exp
    global maxexp
    global level
    global enemy
    global enemyLevel
    global uses
    
    os.system('cls')
    slowprint(f"Ability uses: {uses}")
    slowprint("| Wicked stab, Cost 1 (1) | Coin flip, Cost 2 (2) | Dice roll, Cost 3 (3) | Go back (0)")
    slowprint("What do you do?")
    choice = input("")
    if choice == "1":
        if uses >= 1:
            os.system('cls')
            uses = uses - 1
            damage = damage + (5 + damageUp)
            slowprint(f"You stab the {enemy} wickedly, dealing {damage} damage.")
            slowprint("Press enter to continue")
            input("")
            enemyHealth = enemyHealth - damage
            damage = damage - damage
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            rogueFightAbilities()
        
    elif choice == "2":
        if uses >= 2:
            os.system('cls')
            uses = uses - 2
            choice = random.randint(1, 2)
            if choice == 1:
                damage = damage + 4 + damageUp
                slowprint("You flip your coin and it lands on...")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint("Tails.")
                slowprint(f"You deal {damage} to the {enemy}.")
                enemyHealth = enemyHealth - damage
                damage = damage - damage
            
            elif choice == 2:
                damage = damage + 13 + damageUp
                slowprint("You flip your coin and it lands on...")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint("Heads!")
                slowprint(f"You deal {damage}  to the {enemy}.")
                enemyHealth = enemyHealth - damage
                damage = damage - damage
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            rogueFightAbilities()
    
    elif choice == "3":
        if uses >= 3:
            os.system('cls')
            uses = uses - 3
            choice = random.randint(1,6)
            if choice == 1:
                damage = damage + 0 + damageUp
                slowprint("You roll your dice and...")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint("One.")
                slowprint(f"You deal {damage}  to the {enemy}.")
                enemyHealth = enemyHealth - damage
                damage = damage - damage
        
            elif choice == 2:
                damage = damage + 2 + damageUp
                slowprint("You roll your dice and...")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint("Two.")
                slowprint(f"You deal {damage}  to the {enemy}.")
                enemyHealth = enemyHealth - damage
                damage = damage - damage
            
            elif choice == 3:
                damage = damage + 4 + damageUp
                slowprint("You roll your dice and...")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint("Three.")
                slowprint(f"You deal {damage}  to the {enemy}.")
                enemyHealth = enemyHealth - damage
                damage = damage - damage
            
            elif choice == 4:
                damage = damage + 8 + damageUp
                slowprint("You roll your dice and...")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint("Four.")
                slowprint(f"You deal {damage}  to the {enemy}.")
                enemyHealth = enemyHealth - damage
                damage = damage - damage
            
            elif choice == 5:
                damage = damage + 16 + damageUp
                slowprint("You roll your dice and...")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint("Five.")
                slowprint(f"You deal {damage}  to the {enemy}.")
                enemyHealth = enemyHealth - damage
                damage = damage - damage
            
            elif choice == 6:
                damage = damage + 32 + damageUp
                slowprint("You roll your dice and...")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint("Six!")
                slowprint(f"You deal {damage}  to the {enemy}.")
                enemyHealth = enemyHealth - damage
                damage = damage - damage
        else:
            os.system('cls')
            slowprint("You dont have enough ability uses.")
            slowprint("Press enter to continue")
            input("")
            rogueFightAbilities()
            
    elif choice == "0":
        fight()
            
    slowprint(f"Your health: {playerHealth}/{playerMax} | Level: {enemyLevel} {enemy}s health: {enemyHealth}/{enemyMax}")
    slowprint("Press enter to continue")
    damage = damage - damage
    input("")
    if playerHealth <= 0:
         slowprint("You took too much damage and died.")
         quit()
    else:
        postFight()
    


# Postfight is called upon after having used a ability, this is to prevent ability spam without letting the enemy attack.
    
def postFight():
    global playerHealth
    global playerMax
    global enemyHealth
    global enemyMax
    global enemyStats
    global damage
    global damageUp
    global pots
    global gpots
    global coins
    global exp
    global maxexp
    global level
    global enemy
    global enemyLevel
    global frozen
    global bloodlust
    
    if enemyHealth <= 0:
        os.system('cls')
        damageUp = damageUp - bloodlust
        bloodlust = 0
        enemyHealth = 0
        slowprint(f"You killed the {enemy}!")
        gains = random.randint((enemyStats // 3) * enemyLevel, (enemyStats // 2) * enemyLevel)
        if gains < 1:
            gains = 1
        lower_bound = enemyStats * enemyLevel
        upper_bound = (enemyStats * 2) * enemyLevel

        if lower_bound > upper_bound:
            lower_bound, upper_bound = upper_bound, lower_bound

        gainsexp = random.randint(lower_bound, upper_bound)
        coins = coins + gains
        exp = exp + gainsexp
        slowprint(f"You gained {gains} coins and {gainsexp} experience.")
        enemy = None
        enemyStats = 0
        gains = gains - gains
        gainsexp = gainsexp - gainsexp
        slowprint("Press enter to continue")
        input("")
        if exp >= maxexp:
            os.system('cls')
            exp = exp - exp
            maxexp = maxexp + 254
            damageUp = damageUp + 5
            playerMax = playerMax + 5
            playerHealth = playerMax
            level = level + 1
            slowprint("You leveled up and gained 5 damage and 5 health!")
            slowprint("Press enter to continue:")
            input("")
            if Forest == True:
                forest()
        
            elif Swamps == True:
                swamps()
            
            elif Volcano == True:
                volcano()
        
            elif Dungeon == True:
                dungeon()
    
            else:
                menu()
        if Forest == True:
                forest()
        
        elif Swamps == True:
                swamps()
            
        elif Volcano == True:
                volcano()
        
        elif Dungeon == True:
                dungeon()
    
        else:
            menu()
                
    os.system('cls')
    damage = random.randint(enemyStats, enemyStats * 2)
    slowprint(f"The {enemy} attacks you...")
    if frozen == True:
        slowprint("The enemy is frozen and deals less damage.")
        damage = damage // 2
        frozen = False
    slowprint(f"You take {damage} damage.")
    playerHealth = playerHealth - damage
    print("")
    slowprint(f"Your health: {playerHealth}/{playerMax} | Level: {enemyLevel} {enemy}s health: {enemyHealth}/{enemyMax}")
    slowprint("Press enter to continue")
    damage = damage - damage
    input("")
    if playerHealth <= 0:
         slowprint("You took too much damage and died.")
         quit()
    else:
        fight()
    
    
     
     
#Fight, this is the fight scene where fights play out
    
def fight():
    global playerHealth
    global playerMax
    global enemyHealth
    global enemyMax
    global enemyStats
    global damage
    global damageUp
    global pots
    global gpots
    global coins
    global exp
    global maxexp
    global level
    global enemy
    global enemyLevel
    global bloodlust
    
    os.system('cls')
    while enemyHealth > 0:
        os.system('cls')
        print("| Attack (1) | Heal (2) | Abilites (3) | Run away (0) |")
        slowprint(f"Your health: {playerHealth}/{playerMax} | Level: {enemyLevel} {enemy}s health: {enemyHealth}/{enemyMax}")
        slowprint("What do you do?")
        choice = input("")
        if choice == "1":
            os.system('cls')
            damage = random.randint(5 + damageUp, 10 + damageUp)
            enemyHealth = enemyHealth - damage
            slowprint(f"You attack the {enemy}...")
            slowprint(f"The {enemy} takes {damage} damage.")
            print("")
            slowprint(f"Your health: {playerHealth}/{playerMax} | Level: {enemyLevel} {enemy}s health: {enemyHealth}/{enemyMax}")
            slowprint("Press enter to continue")
            damage = damage - damage
            input("")
            if enemyHealth <= 0:
                os.system('cls')
                damageUp = damageUp - bloodlust
                bloodlust = 0
                enemyHealth = 0
                slowprint(f"You killed the {enemy}!")
                gains = random.randint((enemyStats // 3) * enemyLevel, (enemyStats // 2) * enemyLevel)
                if gains < 1:
                    gains = 1
                lower_bound = (enemyStats * 2) * enemyLevel
                upper_bound = (enemyStats * 5) * enemyLevel

                if lower_bound > upper_bound:
                    lower_bound, upper_bound = upper_bound, lower_bound

                gainsexp = random.randint(lower_bound, upper_bound)
                coins = coins + gains
                exp = exp + gainsexp
                slowprint(f"You gained {gains} coins and {gainsexp} experience.")
                enemy = None
                enemyStats = 0
                gains = gains - gains
                gainsexp = gainsexp - gainsexp
                enemyLevel = enemyLevel - enemyLevel
                slowprint("Press enter to continue")
                input("")
                if exp >= maxexp:
                    os.system('cls')
                    exp = exp - exp
                    maxexp = maxexp + 25
                    damageUp = damageUp + 5
                    playerMax = playerMax + 5
                    playerHealth = playerMax
                    level = level + 1
                    slowprint("You leveled up and gained 5 damage and 5 health!")
                    slowprint("Press enter to continue:")
                    input("")
                if Forest == True:
                    forest()
        
                elif Swamps == True:
                    swamps()
        
                elif Volcano == True:
                    volcano()
        
                elif Dungeon == True:
                    dungeon()
    
                else:
                    menu()
                    
            os.system('cls')
            damage = random.randint(enemyStats, enemyStats * 2)
            playerHealth = playerHealth - damage
            slowprint(f"The {enemy} attacks you...")
            slowprint(f"You take {damage} damage.")
            print("")
            slowprint(f"Your health: {playerHealth}/{playerMax} | Level: {enemyLevel} {enemy}s health: {enemyHealth}/{enemyMax}")
            slowprint("Press enter to continue")
            damage = damage - damage
            input("")
            if playerHealth <= 0:
                slowprint("You took too much damage and died.")
                quit()
            else:
                fight()
            
        if choice == "2":
            os.system('cls')
            print(f"| Health pots: {pots} (1) | Great Health pots: {gpots} (2) | Go back (0) |")
            slowprint("Which one?")
            choice = input("")
            if choice == "1":
                if pots > 0:
                    os.system('cls')
                    pots = pots - 1
                    slowprint("You use one health pot and heal 15 health!")  
                    playerHealth = playerHealth + 15
                    if playerHealth > playerMax:
                        playerHealth = playerMax
                    slowprint("Press enter to continue.")
                    input("")
                    fight()
                else:
                    slowprint("You dont have enough health pots.")
                    slowprint("Press enter to continue.")
                    input("")
                    fight()
            if choice == "2":
                if gpots > 0:
                    os.system('cls')
                    gpots = gpots - 1
                    slowprint("You use one great health pot and heal 30 health!")  
                    playerHealth = playerHealth + 30
                    if playerHealth > playerMax:
                        playerHealth = playerMax
                    slowprint("Press enter to continue.")
                    input("")
                    fight()
                else:
                    slowprint("You dont have enough great health pots.")
                    slowprint("Press enter to continue.")
                    input("")
                    fight()
                    
            elif choice == "0":
                fight()
                
        elif choice == "3":
            os.system('cls')
            if warrior == True:
                warriorFightAbilities()
                
            elif mage == True:
                mageFightAbilities()
                
            elif rogue == True:
                rogueFightAbilities()
                    
            else:
                os.system('cls')
                slowprint("Invalid input.")
                slowprint("Press enter to continue.")
                input("")
                fight()
                
        elif choice == "0":
            os.system('cls')
            slowprint(f"You tried to run away from the {enemy}...")
            slowprint("Press enter to continue")
            input("")
            choice = random.randint(1,2)
            if  choice == 1:
                os.system('cls')
                slowprint("But failed.")
                slowprint("Press enter to continue")
                input()
                postFight()
                
            elif choice == 2:
                os.system('cls')
                slowprint("And succeded!")
                slowprint(f"You got away from the {enemy} safely.")
                slowprint("Press enter to continue")
                input()
                if Forest == True:
                    forest()
        
                elif Swamps == True:
                    swamps()
        
                elif Volcano == True:
                    volcano()
        
                elif Dungeon == True:
                    dungeon()
    
                else:
                    menu()
                    
        else:
            os.system('cls')
            slowprint("Invalid input.")
            slowprint("Press enter to continue.")
            input("")
            fight()
                
    os.system('cls')
    damageUp = damageUp - bloodlust
    bloodlust = 0
    enemyHealth = 0
    slowprint(f"You killed the {enemy}!")
    gains = random.randint((enemyStats // 2) * enemyLevel, enemyStats * enemyLevel)
    if gains < 1:
        gains = 1
    lower_bound = (enemyStats * 2) * enemyLevel
    upper_bound = (enemyStats * 5) * enemyLevel

    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound

    gainsexp = random.randint(lower_bound, upper_bound)
    coins = coins + gains
    exp = exp + gainsexp
    slowprint(f"You gained {gains} coins and {gainsexp} experience.")
    enemy = None
    enemyStats = 0
    gains = gains - gains
    gainsexp = gainsexp - gainsexp
    enemyLevel = enemyLevel - enemyLevel
    slowprint("Press enter to continue")
    input("")
    if exp >= maxexp:
        os.system('cls')
        exp = exp - exp
        maxexp = maxexp + 25
        damageUp = damageUp + 5
        playerMax = playerMax + 5
        playerHealth = playerMax
        level = level + 1
        slowprint("You leveled up and gained 5 damage and 5 health!")
        slowprint("Press enter to continue:")
        input("")
    if Forest == True:
        forest()
        
    elif Swamps == True:
        swamps()
        
    elif Volcano == True:
        volcano()
        
    elif Dungeon == True:
        dungeon()
    
    else:
        menu()
        

#Ability page, here is where you can see your abilites, what they do and how many charges you have

def abilities():
    global uses
    global usesMax
    os.system('cls')
    if warrior == True:
        slowprint("| Shield slam, Costs 1 | Cleave, Costs 2 | Bloodlust, Costs 3 |")
        slowprint(f"Ability uses: {uses}/{usesMax}")
        slowprint("| Learn more (?) | Go back (0) |")
        choice = input("")
        if choice == "?":
            os.system('cls')
            slowprint("Shield slam, Costs 1 use: Deal damage and gain health.")
            slowprint("Cleave, Costs 2: Deal damage depending on enemy health.")
            slowprint("Bloodlust, Costs 3: Temporarily boost your attack.")
            print("")
            slowprint("Press enter to continue")
            input("")
            if Forest == True:
                forest()
        
            elif Swamps == True:
                swamps()
        
            elif Volcano == True:
                volcano()
        
            elif Dungeon == True:
                dungeon()
    
            else:
                menu()
        
        elif choice == "0":
            os.system('cls')
            if Forest == True:
                forest()
        
            elif Swamps == True:
                swamps()
        
            elif Volcano == True:
                volcano()
        
            elif Dungeon == True:
                dungeon()
    
            else:
                menu()
                
        else:
            slowprint("Invalid input")
            slowprint("Press enter to continue: ")
            input("")
            abilities()
        
    elif mage == True:
        slowprint("| Fireball, Costs 1 | Frostbolt, Costs 2 | Song of fire & ice, Costs 3 |")
        slowprint(f"Ability uses: {uses}/{usesMax}")
        slowprint("| Learn more (?) | Go back (0) |")
        choice = input("")
        if choice == "?":
            os.system('cls')
            slowprint("Fireball, Costs 1 use: Deal damage.")
            slowprint("Frostbolt, Costs 2: Deal damage slow down enemy.")
            slowprint("Song of fire & ice, Costs 3: Deal massive damage and slow down enemy.")
            print("")
            slowprint("Press enter to continue")
            input("")
            if Forest == True:
                forest()
        
            elif Swamps == True:
                swamps()
        
            elif Volcano == True:
                volcano()
        
            elif Dungeon == True:
                dungeon()
    
            else:
                menu()
        
        elif choice == "0":
            os.system('cls')
            if Forest == True:
                forest()
        
            elif Swamps == True:
                swamps()
        
            elif Volcano == True:
                volcano()
        
            elif Dungeon == True:
                dungeon()
    
            else:
                menu()
                      
        else:
            slowprint("Invalid input")
            slowprint("Press enter to continue: ")
            input("")
            abilities()
        
    elif rogue == True:
        slowprint("| Wicked stab, Costs 1 | Coin flip, Costs 2 | Dice roll, Costs 3 |")
        slowprint(f"Ability uses: {uses}/{usesMax}")
        slowprint("| Learn more (?) | Go back (0) |")
        choice = input("")
        if choice == "?":
            os.system('cls')
            slowprint("Wicked stab, Costs 1 use: Deal damage.")
            slowprint("Coin flip, Costs 2: Flip a coin, deal damage if you get tails, deal MASSIVE damage if you hit heads.")
            slowprint("Dice roll, Costs 3: Roll a dice, dealing damage depending on what you get.")
            print("")
            slowprint("Press enter to continue")
            input("")
            if Forest == True:
                forest()
        
            elif Swamps == True:
                swamps()
        
            elif Volcano == True:
                volcano()
        
            elif Dungeon == True:
                dungeon()
    
            else:
                menu()
        
        elif choice == "0":
            os.system('cls')
            if Forest == True:
                forest()
        
            elif Swamps == True:
                swamps()
        
            elif Volcano == True:
                volcano()
        
            elif Dungeon == True:
                dungeon()
    
            else:
                menu()
                
        else:
            slowprint("Invalid input")
            slowprint("Press enter to continue: ")
            input("")
            abilities()
                
    


#Shop, here is where you buy health pots to stay alive
    
def shop():
    global coins
    global pots
    global gpots
    os.system('cls')
    print("| Health pot, Costs 2 coins (1) | Health pot upgrad, Costs 5 coins (2) | Go back (0) |")
    slowprint("Welcome to the shop! Here you can buy health pots or upgrade them.")
    slowprint("What do you want to buy?")
    choice = input("")
    if choice == "1":
        if coins >= 2:
            os.system('cls')
            coins = coins - 2
            pots = pots + 1
            slowprint("You bought one health pot! It cost 2 coins.")
            slowprint("Press enter to continue:")
            input("")
            shop()
        else:
            os.system('cls')
            slowprint("You dont have enough coins.")
            slowprint("Press enter to continue.")
            input("")
            shop()
    
    elif choice == "2":
        if coins >= 5:
            os.system('cls')
            coins = coins - 5
            pots = pots - 1
            gpots = gpots + 1
            slowprint("You upgrade one of your health pots! It cost 5 coins")
            slowprint("Press enter to continue:")
            input("")
            shop()
        else:
            os.system('cls')
            slowprint("You dont have enough coins.")
            slowprint("Press enter to continue.")
            input("")
            shop()
            
    elif choice == "0":
        menu()
            
    else: 
        slowprint("Invalid input.")
        shop()



#Inventory, this page shows you your inventory

def inventory():
    os.system('cls')
    print(f"| Coins: {coins} | Health pots: {pots} | Great Health pots: {gpots} |")
    slowprint("Press enter to go back: ")
    input("")
    if Forest == True:
        forest()
        
    elif Swamps == True:
        swamps()
        
    elif Volcano == True:
        volcano()
        
    elif Dungeon == True:
        dungeon()
    
    else:
        menu()
    
    
    
#Stats, this page will show your stats

def stats():
    global Forest
    global Swamps
    global Volcano
    global Dungeon
    global level
    global damage
    global playerHealth
    global playerMax
    global Class
    global maxexp
    
    os.system('cls')
    print(f"| Level {level} | Exp {exp}/{maxexp} | Health: {playerHealth}/{playerMax} | Class: {Class} |")
    slowprint("Press enter to go back: ")
    input("")
    if Forest == True:
        forest()
        
    elif Swamps == True:
        swamps()
        
    elif Volcano == True:
        volcano()
        
    elif Dungeon == True:
        dungeon()
    
    else:
        menu()



def dungeon():
    global Dungeon
    
    os.system('cls')
    
    
    
def volcano():
    global Volcano

    os.system('cls')
    
    
    
# SWAMPS AND ITS MONSTERS
    
    
    
def swampWitch():
    global enemyHealth
    global enemyMax
    global enemyStats
    global enemy
    global enemyLevel
    
    enemyLevel = random.randint(1,3)
    
    enemy = "Swamp witch"
    enemyStats = 5 * enemyLevel
    enemyHealth = enemyStats * 6
    enemyMax = enemyHealth
    
    fight()
    
    
    
def bogDemon():
    global enemyHealth
    global enemyMax
    global enemyStats
    global enemy
    global enemyLevel
    
    enemyLevel = random.randint(1,3)
    
    enemy = "Bog demon"
    enemyStats = 4 * enemyLevel
    enemyHealth = enemyStats * 7
    enemyMax = enemyHealth
    
    fight()
    
    
    
def sunkenUndead(): 
    global enemyHealth
    global enemyMax
    global enemyStats
    global enemy
    
    enemyLevel = random.randint(1,3)
    
    enemy = "Sunken undead"
    enemyStats = 3 * enemyLevel
    enemyHealth = enemyStats * 10
    enemyMax = enemyHealth
    
    fight()
    
    
def swamps():
    global Swamps
    global enemyHealth
    global pots
    global coins
    global exp
    global playerHealth
    global maxexp
    global damageUp
    global playerMax
    global level
    Swamps = True
    
    os.system('cls')
    print("| Continue (1) | Stats (2) | Inventory (3) | Abilities (4) | Go back (0) |")
    slowprint("You find yourself in a deep, dark, murky swamp.")
    slowprint("What do you do?")
    choice = input("")
    if choice == "1":
        encounter = random.randint(1,6)
        if encounter in [1, 2]:
            os.system('cls')
            enemyHealth = 30
            slowprint("You encounter a bog demon!")
            slowprint("Press enter to continue.")
            input("")
            bogDemon()
            
        elif encounter in [3, 4]:
            os.system('cls')
            enemyHealth = 25
            slowprint("You encounter a sunken undead!")
            slowprint("Press enter to continue.")
            input("")
            sunkenUndead()
            
        elif encounter == 5:
            os.system('cls')
            slowprint("You walked through the swamp and found a health pot!")
            pots = pots + 1
            slowprint('"Press enter to continue"')
            input("")
            swamps()
            
        elif encounter == 6:
            os.system('cls')
            slowprint("You walked through the swamp and found a small hut.")
            slowprint("Do you want to raid the swamp hut? Y/N")
            choice = input("")
            if choice in ["Y", "y"]:
                os.system('cls')
                slowprint("You decided to raid the hut.")
                slowprint("Press enter to continue")
                input("")
                choice = random.randint(1,2)
                if choice == 1:
                    os.system('cls')
                    slowprint("The hut was inhabited by a swamp witch and she isnt willing to give up her stuff without a fight.")
                    slowprint("Press enter to conitnue.")
                    input("")
                    swampWitch()
                    
                elif choice == 2:
                    choice = random.randint(1, 10)
                    os.system('cls')
                    slowprint("Lucky for you there was no one inside.")
                    slowprint("You found a chest and inside it some gold!")
                    gains = random.randint(1,4)
                    coins = coins + gains
                    gainsexp = random.randint(10, 15)
                    exp = exp + gainsexp
                    slowprint(f"You gained {gains} coins and {gainsexp} experience.")
                    if exp >= maxexp:
                        os.system('cls')
                        exp = exp - exp
                        maxexp = maxexp + 50
                        damageUp = damageUp + 5
                        playerMax = playerMax + 5
                        playerHealth = playerMax
                        level = level + 1
                        slowprint("You leveled up and gained 5 damage and 5 health!")
                        slowprint("Press enter to continue:")
                        input("")
                        swamps()
                    slowprint("Press enter to continue.")
                    input("")
                    swamps()
                      
            elif choice in ["N", "n"]:
                os.system('cls')
                gainsexp = random.randint(5, 20)
                exp = exp + gainsexp
                slowprint("You decided to go back, but you still got a lil wiser from the journey :)")
                slowprint(f"You gained {gainsexp} experience.")
                slowprint("Press enter to continue.")
                input("")
                if exp >= maxexp:
                        os.system('cls')
                        exp = exp - exp
                        maxexp = maxexp + 50
                        damageUp = damageUp + 5
                        playerMax = playerMax + 5
                        playerHealth = playerMax
                        level = level + 1
                        slowprint("You leveled up and gained 5 damage and 5 health!")
                        slowprint("Press enter to continue:")
                        input("")
                        swamps()
                swamps()
            
    elif choice == "2":
        stats()
        
    elif choice == "3":
        inventory()
        
    elif choice == "4":
        abilities()
    
    elif choice == "0":
        Swamps = False
        menu()
        
    else:
        slowprint("Invalid input.")
        swamps()
    
    
    
#FOREST AND ITS MONSTERS
    


#Spider, triggers a fight with a spider
def spider():
    global enemyHealth
    global enemyMax
    global enemyStats
    global enemy
    global enemyLevel
    
    enemyLevel = random.randint(1,3)
    
    enemy = "Spider"
    enemyStats = 2 * enemyLevel
    enemyHealth = enemyStats * 6
    enemyMax = enemyHealth
    
    fight()
    
                    
                    
#Wolf, triggers a fight with a wolf

def wolf():
    global enemyHealth
    global enemyMax
    global enemyStats
    global enemy
    global enemyLevel
     
    enemyLevel = random.randint(1,3)
    
    enemy = "Wolf"
    enemyStats = 3 * enemyLevel
    enemyHealth = enemyStats * 5
    enemyMax = enemyHealth
    
    fight()
    


#Forest, One of four locations. Hub where you can do location based stuff. 
    
def forest():
    global Forest
    global enemyHealth
    global pots
    global coins
    global exp
    global playerHealth
    global maxexp
    global playerMax
    global damageUp
    global level
    Forest = True
    
    os.system('cls')
    print("| Continue (1) | Stats (2) | Inventory (3) | Abilities (4) | Go back (0) |")
    slowprint("You find yourself in the middle of the forest.")
    slowprint("What do you do?")
    choice = input("")
    if choice == "1":
        encounter = random.randint(1,6)
        if encounter in [1, 2]:
            os.system('cls')
            enemyHealth = 30
            slowprint("You encounter a wolf!")
            slowprint("Press enter to continue.")
            input("")
            wolf()
            
        elif encounter in [3, 4]:
            os.system('cls')
            enemyHealth = 25
            slowprint("You encounter a spider!")
            slowprint("Press enter to continue.")
            input("")
            spider()
            
        elif encounter == 5:
            os.system('cls')
            slowprint("You walked through the forest and found a health pot!")
            pots = pots + 1
            slowprint('"Press enter to continue"')
            input("")
            forest()
            
        elif encounter == 6:
            os.system('cls')
            slowprint("You walked through the forest and found a small lake.")
            slowprint("Do you want to sit down and fish? Y/N")
            choice = input("")
            if choice == "Y" or "y":
                os.system('cls')
                slowprint("You sat down and fished for a while.")
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                slowprint(".", 0.5)
                fish = random.randint(1,3)
                if fish in [1,2]:
                    slowprint("Sadly you didnt catch no fish today")
                    slowprint("Press enter to conitnue.")
                    input("")
                    forest()
                elif fish == 3:
                    slowprint("You caught a fish!")
                    gains = random.randint(1,4)
                    coins = coins + gains
                    gainsexp = random.randint(8, 12)
                    exp = exp + gainsexp
                    slowprint(f"You gained {gains} coins and {gainsexp} experience.")
                    if exp >= maxexp:
                        os.system('cls')
                        exp = exp - exp
                        maxexp = maxexp + 50
                        damageUp = damageUp + 5
                        playerMax = playerMax + 5
                        playerHealth = playerMax
                        level = level + 1
                        slowprint("You leveled up and gained 5 damage and 5 health!")
                        slowprint("Press enter to continue:")
                        input("")
                        forest()
                    slowprint("Press enter to continue.")
                    input("")
                    forest()
                
                
            elif choice in ["N", "n"]:
                os.system('cls')
                gainsexp = random.randint(5, 10)
                exp = exp + gainsexp
                slowprint("You decided to go back, but you still got a lil wiser from the journey :)")
                slowprint(f"You gained {gainsexp} experience.")
                slowprint("Press enter to continue.")
                input("")
                if exp >= maxexp:
                        os.system('cls')
                        exp = exp - exp
                        maxexp = maxexp + 50
                        damageUp = damageUp + 5
                        playerMax = playerMax + 5
                        playerHealth = playerMax
                        level = level + 1
                        slowprint("You leveled up and gained 5 damage and 5 health!")
                        slowprint("Press enter to continue:")
                        input("")
                        forest()
                forest()
            
    elif choice == "2":
        stats()
        
    elif choice == "3":
        inventory()
        
    elif choice == "4":
        abilities()
    
    elif choice == "0":
        Forest = False
        menu()
        
    else:
        slowprint("Invalid input.")
        forest()


#Locations, where to go next

def locations():
    os.system('cls')
    print("| Forest (1) | Swamps (2) | Volcano (3) | Dungeon (4) | Go back (0) |")
    slowprint("Where do you want to go?: ")
    choice = input("")
    if choice == "1":
        forest()
        
    elif choice == "2":
        swamps()
    
    elif choice == "3":
        volcano()
        
    elif choice == "4":
        dungeon()
        
    elif choice == "0":
        menu()
    
    else:
        slowprint("Invalid input.")
        locations()


#Menu, Choose what to do next, main hub
    
def menu():
    os.system('cls')
    global level
    
    print(f"| Locations (1) | Stats (2) | Inventory (3) | Abilities (4) | Shop (5) | Fountain (6) | Save/Reset (7)")
    slowprint("What do you want to do next?: ")
    choice = input("")
    if choice == "1":
        locations()
        
    elif choice == "2":
        stats()
        
    elif choice == "3":
        inventory()
        
    elif choice == "4":
        abilities()
        
    elif choice == "5":
        shop()
        
    elif choice == "6":
        fountain()
        
    elif choice == "7":
        saveResetLoad()
    
    else:
        slowprint("Invalid input.")
        menu()
        


#Class Pick, Here you pick your class

def classPick():
    global warrior
    global mage
    global rogue
    global playerHealth
    global playerMax
    global Class
    global damageUp
    
    slowprint("Before we begin the adventure you need to pick a class.")
    print("________")
    slowprint("""Warrior (1)
Mage    (2)
Rogue   (3)""")
    print("________")
    slowprint("Which one?: ")
    choice = input("")
    if choice == "1":
        playerHealth = 80
        playerMax = 80
        warrior = True
        Class = "Warrior"
        menu()
        
    elif choice == "2":
        playerHealth = 60
        playerMax = 60
        mage = True
        damageUp = damageUp + 3
        Class = "Mage"
        menu()
        
    elif choice == "3":
        playerHealth = 50
        playerMax = 50
        rogue = True
        damageUp = damageUp + 5
        Class = "Rogue"
        menu()
        
    else:
        slowprint("Invalid input.")
        classPick()
        
    
    
#This is where it starts
    
slowprint("Welcome to Terror Rock!")
slowprint("Press enter to begin: ")
input("")
os.system('cls')
classPick()