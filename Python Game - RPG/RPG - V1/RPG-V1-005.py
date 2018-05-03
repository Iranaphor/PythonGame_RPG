import random
import time

#Stats
baseDamage = 2
ownDamage = 1
maxHealth = 100000
ownHealth = 15
ownDefence = 0
#Weapons
fistAttack = 0
swordAttack = 10
maceAttack = 13
weaponDamage = 0
weaponDefence = 0
#Skills
attackLevel = 10
attackExp = 0
defenceLevel = 10
defenceExp = 0
#EntityStats
creatureDamage = 1
creatureHealth = 100
#EntityDrops
batAttackExp = 1
batDefenceExp = 1

#####################

#Items:
torch = False
forestBoots = False
waterStaff = False
getTorch = True
#MainQuests:
townHallDoor = "shut"
realLocation = "Square"

#Quests:
lostChild = "lost"

#AreaMessages:
townHallGreet = True
townHallDoor = True

#EasterEggs:
swimCounter = 0
#####################

def getTorch():
    if(getTorch):
        print("Walking out of the town hall you hear a voice bahind you.")
        print("The Mayor's assistant becons you from the doorway.")
        print("\"Don't forget this.\"")
        print("He throws a torch at you.")
        torch = False

def mayorSpeech1():
    print("\"Go away, I'm busy!\"")
    print("You knock on the door again.")
    print("The mayor, opens the door, wearing his Mayor Hat.")
    print("He has his arms full with dead birds")
    print("\"Wh\t do you want?\"")
    print("You explain that you woke up here and was told to come see him.")
    print("He looks down at the pile of birds he is holding.")
    print("\"I may have a job or you.\"")
    print("\"Go to the caves North of the square and speak to Delwick sitting at the entrance.")
    print("\"Tell him the password: \"146\" and he will explain what you need to do.\"")                        
    print("When you are done, come back and see me.")


def weapon():
    print ()
    print ("What weapon would you like to use?")
    print ("Fist ¦ Sword ¦ Mace")
    weaponChoice = input("Weapon Choice: ")
    if (weaponChoice.lower() == "fist"):
        weaponDamage = fistAttack
        weaponDefence = 0
    if (weaponChoice.lower() == "sword"):
        weaponDamage = swordAttack
        weaponDefence = 5
    if (weaponChoice.lower() == "mace"):
        weaponDamage = maceAttack
        weaponDefence = 3

def resetBat():
    creatureDamage = 1
    creatureHealth = 100

def objectInspection():
    if (object == "Hostile_Bat"):
        print ("This bat looks like it might attack you...")

#####################
"""
print("You awaken in a small park.")
time.sleep(1.4)
print("You sit up and look arround...")
time.sleep(1.4)
print("To the North is a cave entrance.")
time.sleep(1.4)
print("To the East is a dense forest too thick to walk through.")
time.sleep(1.4)
print("To the South is the sea.")
time.sleep(1.4)
print("To the West is a man giving you a funny expression.")
time.sleep(1.4)
print("The man walks up to you.")
time.sleep(1.4)
"""
print("\"I dont recognise you, are you new?\"")
time.sleep(1)
choice1 = input("(Y/N): ")
if (choice1.upper() == "Y"):
    print("\"Well then, welcome to our small village.\"")
else:
    print("\"Well I never normally forget a face. Sorry...\"")

print("\"You should go and speak to our mayor.\"")
print("\"He is in the town hall just west of here.\"")

#Locations and Story...
alive = True
while (alive == True):
    realLocation = "Square"
    location = realLocation
    while (location == "Square"):
        print("What direction would you like to go in?")
        direction = input("(N|S|E|W): ")

        if (direction.upper() == "N"):
            if (torch == True):
                realLocation = "Cave"
                
            else:
                print("You need a torch to go there...")
                realLocation = "Square"
        if (direction.upper() == "E"):
            if (forestBoots == True):
                realLocation = "Forest"
            else:
                print("You need some stronger boots to go there...")
                realLocation = "Square"
        if (direction.upper() == "S"):
            if (waterStaff == True):
                realLocation = "SeaTemple"
            else:
                swimCounter = swimCounter + 1
                if (swimCounter == 3):
                    print("Ok then, but only a quick swim!")
                    print("You go down to the beach, get changed and dive into the water.")
                    print("The water was freezing.")
                    print("You jump out, get dried and head back to the square.")
                    print("There is no way that we are going back into that water!")
                else:
                    print("It would not be wise to swim at this point in time...")
                realLocation = "Square"

######################################################################################################################################
                
        if (direction.upper() == "W"):
            realLocation = "Town Hall"
            while (realLocation == "Town Hall"):

                if (townHallGreet == True):
                    print("You walk to the west and see the town hall ahead.")
                    print("Welcome to the Town Hall!")            
                    townHallGreet = False

                choiceOpenTownHallDoor = int(input("(Open the Town Hall door (1)¦ Leave the door alone (2)):"))
                while (choiceOpenTownHallDoor == 1):
                    print("You go up to the door and try to push it open.")
                    print("It is stuck.")
                    print("What would you like to do?")

                    if (townHallDoor == True):
                        choiceTownHallDoor = int(input("(Push harder (1)¦ Look round the back (2)¦ Knock on the door(3)): "))
                        
                    if(choiceTownHallDoor == 1):
                        print("You push harder and the door budges slightly.")
                        print("You hear a voice...")
                        mayorSpeech1()
                        townHallDoor = False
                        choiceTownHallDoor = 0
                        
                    if(choiceTownHallDoor == 2):
                        if(lostChild == "lost"):
                            print("You look round the back of the Town Hall and see a child crying on the step.")
                            choiceLostChild = int(input("(Speak to the Child (1)¦ Go back to the town hall (2)): " ))
                            if(choiceLostChild == 1):
                                print("You ask the child what is wrong?")
                                print("\"I cant find my doggy!\"")
                                print("\"Will you look for my doggy for me?\"")
                                choiceLostDog = int(input("(Sure (1)¦ No way (2)): "))
                                if (choiceLostDog == 1):
                                    print("\"Thanks mister!\"")
                                    print("The boy stopped crying and ran off happy.")
                                if (choiceLostDog == 2):
                                    print("\"Why are you so mean!\"")
                                    print("After shouting at you he went back to crying...")
                                print("Finding that lost dog may make the child happier.")
                                print("You add the quest to your quest log.")
                            if(choiceLostChild == 2):
                                print("You head back to the town hall.")
                        else:
                            print("You find nothing behind the Town Hall")
                        choiceTownHallDoor = 0
                            
                    if (choiceTownHallDoor == 3):
                        print("You knock on the large wooden door and you hear a voice...")
                        time.sleep(3)
                        mayorSpeech1()
                        townHallDoor = False
                        choiceTownHallDoor = 0

                    realLocation = "Square"
                    getTorch()
            
                if(choiceOpenTownHallDoor == 2):
                    print("You do nothing")
                    realLocation = "Square"
                    
        print("You head back into the square.")
        print("Real Location: ", realLocation)
        print("Location: ", location)
        location = realLocation            
        
            
#####################

"""

print ("You encounter a Hostile Bat.")
print ("It flies past you.")
print ("Would you like to inspect the Hostile Bat?")

inspection = input("(Y/N):  ")
if (inspection.upper() == "Y"):
    objectInspection()

print()
print ("The Hostile Bat comes back towards you.")
print ("Leftclick to Fight | Rightclick to Run")
decision = input("Decision: ")
print ()

while(decision.lower() == "rightclick"):
    print("You run out of the cave and fail the quest...")
    break
if(decision.lower() == "leftclick"):
    resetBat()
    weapon()
    maxHealth = defenceLevel + weaponDefence + 20
    ownHealth = maxHealth
while (decision.lower() == "leftclick"):
    resetBat()
    while (creatureHealth > 0):
        ownDamage = (baseDamage + weaponDamage + attackLevel + (int(random.random() * 10 ) - 5))
        attackChance = int(random.random() * 10)
        print()
        print()
        print ("You swing your weapon!")
        time.sleep(2)
        if (attackChance > 3):
            creatureHealth = creatureHealth - ownDamage
            print ("You damaged the creature by, ", ownDamage)
            attackExp = attackExp + batAttackExp
            if (creatureHealth < 0):
                creatureHealth = 0
            print ("The CREATURE'S health is now at: ", creatureHealth)
            if (attackExp == 10):
                attackLevel = attackLevel + 1
                attackExp = 0
                print ()
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Congratulations!")
                print ("Your Attack Level has been raised!")
                print ("Your Attack Level is now at:", attackLevel)
                print ("You now deal additional Damage during a fight.")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print ("You missed!")
            print ("The creature did damage to you.")
            ownHealth = ownHealth - creatureDamage
            print ("YOUR health is now at: ", ownHealth)
            defenceExp = defenceExp + batDefenceExp
            if (defenceExp == 10):
                defenceLevel = defenceLevel + 1
                maxHealth = defenceLevel + 20
                ownHealth = maxHealth
                print ()
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("Congratulations!")
                print ("Your Defence Level has been raised!")
                print ("Your Defence Level is now at: ", defenceLevel)
                print ("Your health has been increased to: ",maxHealth)
                print ("And your health has been restored to its new maximum.")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while (creatureHealth == 0):
        print ()
        print ("You have slain the creature!")
        print ("Another bat comes out of the darkness, would you like to attack it?")
        print ("Leftclick to Fight | Rightclick to Leave")
        decision = input()    
        if(decision.lower() == "rightclick"):
            print("Return to your adventure another day!")
            break
        creatureHealth = 100

"""
#include random percentage drop rates for items, also include item quantities
