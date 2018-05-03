import random
import time

#import http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5
file = 1
if (file == 1):
    savedGame = open('progress.txt', 'r')
    savedGame.readline()
    xLocation = int(savedGame.readline())
    savedGame.readline()
    yLocation = int(savedGame.readline())
    savedGame.readline()
    zLocation = int(savedGame.readline())
    savedGame.readline()
    location = str(savedGame.readline())

    savedGame.readline()
    savedGame.readline()
    currentHelmType = int(savedGame.readline())
    savedGame.readline()
    currentBodyType = int(savedGame.readline())
    savedGame.readline()
    currentLegsType = int(savedGame.readline())
    savedGame.readline()
    currentBootType = int(savedGame.readline())

    savedGame.readline()
    savedGame.readline()
    currentWeapon = int(savedGame.readline())
    savedGame.readline()
    weapons = savedGame.readline()
    savedGame.readline()

    savedGame.close()
######################################################################################################################################
#Settings
textSpeed = 1.5
######################################################################################################################################
#Location
#xLocation = int(0)
#yLocation = int(0)
#zLocation = int(0)
locationName = ["Square", "Town Hall", "Cave Entrance", "Caves Ladder Room", "Forest Edge", "Forest", "Beach", "Sea", "Behind Town Hall", "Cave Tunnels Entrance", "Coast", "Deep Tunnels"]
#location = locationName[0]
######################################################################################################################################
#Armour
armourTypes = ("Empty Slot", "Cloth", "Iron", "Steel", "Gold", "Mithril", "Alanite")
#currentHelmType = 0
helmDefence = ("+0", "+1", "+2", "+4", "+6", "+9", "+13")
helmDefenceLV = (0, 1, 2, 4, 6, 9, 13)
#currentBodyType = 1
bodyDefence = ("+0", "+3", "+4", "+7", "+9", "+13", "+19")
bodyDefenceLV = (0, 3, 4, 7, 9, 13, 19)
#currentLegsType = 1
legsDefence = ("+0", "+1", "+2", "+4", "+6", "+9", "+16")
legsDefenceLV = (0, 1, 2, 4, 6, 9, 16)
#currentBootType = 1
bootDefence = ("+0", "+1", "+2", "+4", "+6", "+9", "+13")
helmDefenceLV = (0, 1, 2, 4, 6, 9, 13)
######################################################################################################################################
#Weapons
#weapons = ["Fist", "Torch", "Sword"]
#currentWeapon = 0
weaponTypes = ["Melee", "Melee", "Melee"]
weaponDamages = ["+0", "+3", "+8"]
weaponDamagesLV = (0, 3, 8)
activeWeapon = ["*Equipped*", "", ""]
######################################################################################################################################
#Bag Items
    #Food
rawSalmon = 8
salmon = 2
crab = 3
foodBagCapacity = 15
    #Armour
armourBagCapacity = 5
clothHelm = False
swimWear = True
ironBoots = False
townHallAccess = True

    #Weapons / Tools
weaponBagCapacity = 5
torch = True

    #Items
itemsBagCapacity = 30
itemsList = ["Stick ", "Stone "]
itemQuant = [4, 5]

    #Bank
bankSize = 150
bankedItems = ["Bread ","Pie   ","Butter",]
bankedItemsQuant = [6,4,3]
######################################################################################################################################
#Bank
#def bank(itemsList, itemQuant, itemsBagCapacity, bankedItems, bankedItemsQuant, bankSize):

######################################################################################################################################
#Maps
def Location_Square():
    print("█               ▄       ▄         ")
    print("█       █████████   N   █████████ ")
    print("█       ██                     ██       Caves      (N)")
    print("█       ██                     ██ ")
    print("█       ██                     ██       Forest     (E)")
    print("█      ▀▀▀                     ▀▀▀")
    print("█                                       Beach      (S)")
    print("█       W                       E ")
    print("█                                       Town Hall  (W)")
    print("█      ▄▄▄                     ▄▄▄")
    print("█       ██                     ██ ")
    print("█       ██                     ██ ")
    print("█       ██                     ██ ")
    print("█       █████████   S   █████████ ")
    print("█               ▀       ▀         ")
    return

def Location_Caves():
    print()
    print("       █████████████████████████ ")
    print("       ██                     ██       Square     (S)")
    print("       ██                     ██ ")
    print("       ██                     ██       Ladder     (D)")
    print("       ██                     ██ ")
    print("       ██        ╔═══╗        ██ ")
    print("       ██        ║ L ║        ██ ")
    print("       ██        ╚═══╝        ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       █████████   S   █████████ ")
    print("               ▀       ▀         ")
    return

def Location_Caves_LadderRoom():
    print("               ▄       ▄         ")
    print("       █████████   N   █████████ ")
    print("       ██                     ██       Cave Tunnels (N)")
    print("       ██                     ██ ")
    print("       ██                     ██       Cave River   (E)")
    print("       ██                     ▀▀▀")
    print("       ██        ╔═══╗                 Ladder       (U)")
    print("       ██        ║ L ║         E ")
    print("       ██        ╚═══╝           ")
    print("       ██                     ▄▄▄")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       █████████████████████████ ")
    print()
    return

def Location_Cave_Tunnels_1():
    print("               ▄       ▄         ")
    print("       █████████   N   █████████ ")
    print("       ██                     ██       Deep Caves   (N)")
    print("       ██                     ██ ")
    print("       ██                     ██       Ladder Room  (S)")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       █████████   S   █████████ ")
    print("               ▀       ▀         ")
    return
def Location_TownHall():
    print("               ▄       ▄         ")
    print("       █████████   N   █████████ ")
    print("       ██                     ██       Bank (N)")
    print("       ██                     ██ ")
    print("       ██                     ██       Town Square       (E)")
    print("      ▀▀▀                     ▀▀▀")
    print("                                       Town Hall Door    (W)")
    print("       W                       E ")
    print("                                 ")
    print("      ▄▄▄                     ▄▄▄")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       █████████████████████████ ")
    print()
    return

def Location_Town_Bank():
    print()
    print("Use [Inspect (2)] to access the bank.")
    print()
    print("       █████████████████████████ ")
    print("       ██                     ██       Town Hall   (S)")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       █████████   S   █████████ ")
    print("               ▀       ▀         ")
    return

def Location_ForestEntrance():
    print()
    print("       █████████████████████████ ")
    print("       ██                     ██       Forest       (E)")
    print("       ██                     ██ ")
    print("       ██                     ██       Town Square  (W)")
    print("      ▀▀▀                     ▀▀▀")
    print("                                 ")
    print("       W                       E ")
    print("                                 ")
    print("      ▄▄▄                     ▄▄▄")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       █████████████████████████ ")
    print()
    return

def Location_Forest2():
    print("               ▄       ▄         ")
    print("       █████████   N   █████████ ")
    print("       ██                     ██       Forest  (N)")
    print("       ██                     ██ ")
    print("       ██                     ██       Forest  (E)")
    print("      ▀▀▀                     ▀▀▀")
    print("                                       Forest  (S)")
    print("       W                       E ")
    print("                                       Forest  (W)")
    print("      ▄▄▄                     ▄▄▄")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       ██                     ██ ")
    print("       █████████   S   █████████ ")
    print("               ▀       ▀         ")
    return

def Location_Beach():
    print("               ▄       ▄         ")
    print("       █████████   N   █████████ ")
    print("       ██                     ██       Square          (N)")
    print("       ██                     ██ ")
    print("       ██                     ██       Seafront Shops  (E)")
    print("      ▀▀▀                     ▀▀▀")
    print("                                       Sea  (S)")
    print("       W                       E ")
    print("                                       Forest  (W)")
    print("       ------------------------- ")
    print("       ------------------------- ")
    print("       ------------------------- ")
    print("       ------------------------- ")
    print("       ----------  S  ---------- ")
    print()
    return

def Location_Coast():
    print()
    print("       ----------  N  ---------- ")
    print("       -------------------------       Beach    (N)")
    print("       ------------------------- ")
    print("       -------------------------       Coast    (E)")
    print("       ------------------------- ")
    print("         ---------------------         Deep Sea (S)")
    print("       W --------------------- E ")
    print("         ---------------------         Coast    (W)")
    print("       ------------------------- ")
    print("       ------------------------- ")
    print("       ------------------------- ")
    print("       ========================= ")
    print("       ==========  S  ========== ")
    print()
    return

def Location_Sea():
    print()
    print("       ==========  N  ========== ")
    print("       =========================       Beach    (N)")
    print("       ========================= ")
    print("       =========================       Sea      (E)")
    print("       ========================= ")
    print("         =====================         Sea      (S)")
    print("       W ===================== E ")
    print("         =====================         Deep Sea (W)")
    print("       ========================= ")
    print("       ========================= ")
    print("       ========================= ")
    print("       ========================= ")
    print("       ==========  S  ========== ")
    print()
    return


######################################################################################################################################
#Equipment
def Equipment():
    currentWeapon = 0
    equipmentVar = 0
    while(equipmentVar == 0):
        print()
        print("Equipment Options:")
        equipmentChoice1 = int(input("[View Armour (1) ¦ View Weapons (2) ¦ View Bag (3) ¦ Return (4)]: "))
        if (equipmentChoice1 == 1): #ViewArmour
            print()
            print("Helm:   ",armourTypes[currentHelmType])
            print("Body:   ",armourTypes[currentBodyType])
            print("Legs:   ",armourTypes[currentLegsType])
            print("Boot:   ",armourTypes[currentBootType])
            equipmentVar2 = 0
            while(equipmentVar2 == 0):
                print()
                print()
                print()
                print("More Information:")
                armourChoice1 = int(input("[Helm Stats (1) ¦ Body Stats (2) ¦ Legs Stats (3) ¦ Boot Stats (4) ¦ Return (5)]: "))
                if(armourChoice1 == 1):
                    print()
                    print("Helm  Type: ",armourTypes[currentHelmType])
                    print("Helm Defence: ",helmDefence[currentHelmType])
                elif (armourChoice1 == 2):
                    print()
                    print("Helm Type: ",armourTypes[currentBodyType])
                    print("Helm Defence: ",helmDefence[currentBodyType])
                elif (armourChoice1 == 3):
                    print()
                    print("Legs Type: ",armourTypes[currentLegsType])
                    print("Legs Defence: ",legsDefence[currentLegsType])
                elif (armourChoice1 == 4):
                    print()
                    print("Boot Type: ",armourTypes[currentBootType])
                    print("Boot Defence: ",bootDefence[currentBootType])
                elif (armourChoice1 == 5):
                    print()
                    print("~~~Previous menu opened.~~~")
                    equipmentVar2 = 1
                else:
                    print()
                    print("That is not a valid response.")
        elif (equipmentChoice1 == 2):#ViewWeapons
            while (equipmentChoice1 == 2):
                print()
                print()
                print("Current Weapon:    ", weapons[currentWeapon])
                print()
                print("Weapon Options:")
                weaponChoice1 = int(input("[List Weapons (1) ¦ Get Weapon Stats (2) ¦ Return (3)]: "))
                if (weaponChoice1 == 1):#ListWeapons
                    print()
                    print("Owned Weapons:")
                    weaponslist = int(0)
                    while (weaponslist < len(weapons)):
                        print((weaponslist + 1), "): ", weapons[weaponslist], "    ", activeWeapon[weaponslist])
                        weaponslist = weaponslist + 1
                    print()
                    weaponChoiceVar2 = 0
                    while(weaponChoiceVar2 == 0):
                        print("Weapon Choices: ")
                        weaponChoice2 = int(input("[Swap Weapons (1)¦ Return (2)]: "))
                        if (weaponChoice2 == 1):#SwapWeapons
                            print()#Fill in
                            print("What weapon would you like to swap with? [1 ~", len(weapons) , "]:")
                            swapChoice = int(input("Swap Number: "))
                            if (swapChoice < len(weapons) + 1) and (swapChoice > 0): #If valid answer
                                activeWeapon[currentWeapon] = ""
                                currentWeapon = swapChoice - 1
                                activeWeapon[currentWeapon] = "*Equipped*"
                                print()
                                print("These are the statistics for your now equipped weapon.")
                                print("Weapon: ", weapons[currentWeapon])
                                print("Type:   ", weaponTypes[currentWeapon])
                                print("Damage: ", weaponDamages[currentWeapon])
                            else:#Error
                                print()
                                print("That is not a valid response.")
                            weaponChoiceVar2 = 1
                        elif (weaponChoice2 == 2):#Return
                            print()
                            print("~~~Previous menu opened.~~~")
                            weaponChoiceVar2 = 1
                        else:#Error
                            print()
                            print("That is not a valid response.")
                            weaponChoiceVar2 = 1

                    equipmentChoice1 = 0
                elif (weaponChoice1 == 2):#GetWeaponStats
                    print()
                    print("These are the statistics for your current weapon.")
                    print("Weapon: ", weapons[currentWeapon])
                    print("Type:   ", weaponTypes[currentWeapon])
                    print("Damage: ", weaponDamages[currentWeapon])
                    equipmentChoice1 = 0
                elif (weaponChoice1 == 3):#Return
                    print()
                    print("~~~Previous menu opened.~~~")
                    equipmentChoice1 = 0
                else:#Error
                    print()
                    print("That is not a valid response.")
        elif (equipmentChoice1 == 3):#ViewBag
            print()
            bagVar1 = 0
            while(bagVar1 == 0):
                print("What pouch would you like to view: ")
                bagChoice = int(input("[Food(1) ¦ Armour (2) ¦ Weapons/Tools (3) ¦ Items (4) ¦ Quest Items (5) ¦ Return (6)]: "))
                if(bagChoice == 1):#Food
                    print()
                elif(bagChoice == 2):#Armour
                    print()
                elif(bagChoice == 3):#Weapons/Tools
                    print()
                elif(bagChoice == 4):#Items
                    print()
                    print("Pouch Items:")
                    itemsListVar1 = int(0)
                    while (itemsListVar1 < len(itemsList)):
                        print((itemsListVar1 + 1), ") ", itemsList[itemsListVar1], "    ->    ", itemQuant[itemsListVar1])
                        itemsListVar1 = itemsListVar1 + 1
                    print()
                    print("Pouch Quantity: ", sum(itemQuant), " /50")   #INC Custom Bag Pouches
                    itemChoiceVar = 0
                    while(itemChoiceVar == 0):
                        print("What would you like to do: ")
                        itemChoiceVar2 = int(input("[Drop Item (1) ¦ Use Item (2) ¦ Inspect (3) ¦ Return (4)]"))
                        print()
                        if(itemChoiceVar2 == 1):#DropItem
                            print("What item would you like to drop? [1 ~", len(itemsList), "]:")
                            itemDropID = int(input("Item ID to Drop: "))
                            if(itemDropID < len(weapons) + 1) and (itemDropID > 0): #If valid answer)
                                itemDropQuantVar = 0
                                while(itemDropQuantVar == 0):
                                    print()
                                    print("How many of", itemsList[itemDropID - 1], "would you like to drop? [1 ~", itemQuant[itemDropID - 1], "]:")
                                    itemDropQuant = int(input("Number of items to drop: "))
                                    if(itemDropQuant <= itemQuant[itemDropID - 1]) and (itemDropQuant >= 0):
                                        if (itemDropQuant == 0):
                                            print()
                                            print("You have dropped nothing.")
                                        else:
                                            itemQuant[itemDropID - 1] = itemQuant[itemDropID - 1] - itemDropQuant
                                            itemDropQuantVar = 1
                                            print()
                                            print("You have dropped", itemDropQuant, "of", itemsList[itemDropID - 1])
                                            print("You have", itemQuant[itemDropID - 1], "remaining.")
                                            print()
                                    else: #Error
                                        print()
                                        print("That is not a valid response.")
                            else:#Error
                                print()
                                print("That is not a valid response.")

                        elif(itemChoiceVar2 == 2):#UseItem
                            ...
                        elif(itemChoiceVar2 == 3):#Inspect
                            ...
                        elif(itemChoiceVar2 == 4):#Return
                            print()
                            print("~~~Previous menu opened.~~~")
                            itemChoiceVar = 1
                        else:#Error
                            print()
                            print("That is not a valid response.")
                    print()
                elif(bagChoice == 5):#QuestItems
                    print()
                elif(bagChoice == 6):#Return
                    print()
                    print()
                    print("~~~Previous menu opened.~~~")
                    bagVar1 = 1
                else:#Error
                    print()
                    print("That is not a valid response.")
        elif (equipmentChoice1 == 4):#Return
            print()
            print("~~~Previous menu opened.~~~")
            equipmentVar = 1
        else:#Error
            print()
            print("That is not a valid response.")
    return


######################################################################################################################################
#Actions
alive = True
while (alive == True):
    print("█")
    print("█ What would you like to do?")
    if (xLocation == 0) and (yLocation == 0) and (zLocation == 0):#1
        Location_Square()
    elif (xLocation == -1) and (yLocation == 0) and (zLocation == 0):#2
        Location_TownHall()
    elif (xLocation == -1) and (yLocation == 1) and (zLocation == 0):#3
        Location_Town_Bank()
    elif (xLocation == 0) and (yLocation == 1) and (zLocation == 0):#4
        Location_Caves()
    elif (xLocation == 0) and (yLocation == 1) and (zLocation == -1):#5
        Location_Caves_LadderRoom()
    elif (xLocation == 0) and (yLocation == 2) and (zLocation == -1):
        Location_Cave_Tunnels_1()
    elif (xLocation == 1) and (yLocation == 0) and (zLocation == 0):
        Location_Forest_Entrance()
    elif (xLocation == 2) and (yLocation == 0) and (zLocation == 0):
        Location_Forest2()
    elif (xLocation == 0) and (yLocation == -1) and (zLocation == 0):
        Location_Beach()
    elif (xLocation == 0) and (yLocation == -1) and (zLocation == 0):
        Location_Coast()
    elif (xLocation == 0) and (yLocation == -3) and (zLocation == 0):
        Location_Sea()
    else:
        print()
    actionChoice = input("█   [Move (1) ¦ Inspect (2) ¦ Equipment (3) ¦ Exit Game (4)]: ")
    if (actionChoice == "1"):#Move
        movementVar0 = 0
        while(movementVar0 == 0):
            if ((xLocation == 0) and (yLocation == 0) and (zLocation == 0)): #Square
                print()
                print("What direction would you like to move in?")
                moveDirection = input("[North (N) ¦ South (S) ¦ East (E) ¦ West(W) ¦ Return (R)]: ")
                print()
                if (moveDirection.upper() == "N"):
                    if (torch == True):
                        yLocation = yLocation + 1
                        print("You have moved North to the Cave Entrance")
                        location = locationName[2]
                        break
                    else:
                        print("You need a light source to go into those caves.")
                elif (moveDirection.upper() == "S"):
                    if (swimWear == True):
                        yLocation = yLocation - 1
                        print("You have moved South to the Beach")
                        location = locationName[6]
                        break
                    else:
                        print("That water looks too cold to swim in this time of year.")
                elif (moveDirection.upper() == "E"):
                    if (ironBoots == True):
                        xLocation = xLocation + 1
                        print("You have moved East to the Forest Entrance.")
                        location = locationName[4]
                        break
                    else:
                        print("You need some stronger boots to go in there.")
                elif (moveDirection.upper() == "W"):
                    if (townHallAccess == True):
                        xLocation = xLocation - 1
                        print("You have moved west to the Town Hall.")
                        location = locationName[1]
                        break
                    else:
                        print("You have not currently got permission to go to the Town Hall")
                elif (moveDirection.upper() == "R"):
                    print("~~~Previous menu opened.~~~")
                    movementVar0 = 1
                else:
                    print("That is not a valid response.")
                    movementVar0 = 1

            elif (xLocation == -1) and (yLocation == 0) and (zLocation == 0): #TownHall
                print()
                print("What direction would you like to move in?")
                moveDirection = input("[North (N) ¦ East (E) ¦ Return (R)]: ")
                print()
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("You have moved North to the Town Bank")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "E"):
                    xLocation = xLocation + 1
                    print("You have moved East back to the Square.")
                    location = locationName[4]
                    break
                elif (moveDirection.upper() == "R"):
                    print("~~~Previous menu opened.~~~")
                    movementVar0 = 1
                else:
                    print("That is not a valid response.")

            elif (xLocation == -1) and (yLocation == 1) and (zLocation == 0):  #Town_Bank
                print()
                print("What direction would you like to move in?")
                moveDirection = input("[South (S) ¦ Return (R)]: ")
                print()
                if (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("You move South to the Town Hall.")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "R"):
                    print("~~~Previous menu opened.~~~")
                    movementVar0 = 1
                else:
                    print("That is not a valid response.")

            elif (xLocation == 0) and (yLocation == 1) and (zLocation == 0): #Cave Entrance
                print()
                print("What direction would you like to move in?")
                moveDirection = input("[South (S) ¦ Climb down Ladder (D) ¦ Return (R)]: ")
                print()
                if (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("You move South back to the Square.")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "D"):
                    zLocation = zLocation - 1
                    print("You climb down the ladder to a lower floor in the cave.")
                    location = locationName[4]
                    break
                elif (moveDirection.upper() == "R"):
                    print("~~~Previous menu opened.~~~")
                    movementVar0 = 1
                else:
                    print("That is not a valid response.")

            elif (xLocation == 0) and (yLocation == 1) and (zLocation == -1): #Caves Floor LadderRoom
                print()
                print("What direction would you like to move in?")
                moveDirection = input("[North (N) ¦ Climb up Ladder (U) ¦ East (E) ¦ Return (R)]: ")
                print()
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation - 1
                    print("You move North further into the Cave Tunnels.")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "U"):
                    zLocation = zLocation - 1
                    print("You climb up the ladder to the Cave Entrance.")
                    location = locationName[4]
                    break
                elif (moveDirection.upper() == "E"):
                    zLocation = zLocation - 1
                    print("You move out of the cave arriving at a river.")
                    location = locationName[4]
                    break
                elif (moveDirection.upper() == "R"):
                    print("~~~Previous menu opened.~~~")
                    movementVar0 = 1
                else:
                    print("That is not a valid response.")

            elif (xLocation == 0) and (yLocation == 2) and (zLocation == -1): #Cave Tunnels
                print()
                print("What direction would you like to move in?")
                moveDirection = input("[North (N) ¦ South (S) ¦ Return (R)]: ")
                print()
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("You move further into the tunnels.")
                    location = locationName[11]
                    break
                elif (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("You move South making your way back to the room with the Ladder.")
                    location = lcationName[3]
                    break
                elif (moveDirection.upper() == "R"):
                    print("~~~Previous menu opened.~~~")
                    movementVar0 = 1
                else:
                    print("That is not a valid response.")
    elif (actionChoice == "2"):#Inspect
        print()
        if (xLocation == -1) and (yLocation == 1) and (zLocation == 0):
            tempVarLoop1 = 0
            while (tempVarLoop1 == 0):
                itemsListVar1 = int(0)
                print("  Pouch Inventory:")
                while (itemsListVar1 < len(itemsList)):
                    print("    ", (itemsListVar1 + 1), ") ", itemsList[itemsListVar1], "    ->    ", itemQuant[itemsListVar1])
                    itemsListVar1 = itemsListVar1 + 1
                print("  Pouch Quantity: ", sum(itemQuant), "/30")
                print()
                print("  Bank Inventory:")
                bankListVar1 = int(0)
                while (bankListVar1 < len(bankedItems)):
                    print("    ", (bankListVar1 + 1), ") ", bankedItems[bankListVar1], "    ->    ", bankedItemsQuant[bankListVar1])
                    bankListVar1 = bankListVar1 + 1
                print("  Bank Quantity: ", sum(bankedItemsQuant), "/150")
                print()
                print()
                choice = input("[Withdraw (W) ¦ Deposit (D) ¦ Close Bank (C)]: ")
                if (choice.upper() == "W"):#Withdraw
                    print()
                    if (len(bankedItems) == 0):
                        print("Your bank is currently empty, you cannot withdraw from it.")
                        print()
                        tempVarBankWithdrawEmpty = input("Click Return (Enter) to coninue: ")
                    else:
                        witemID = int(input("Item to withdraw: "))
                        wquantity = int(input("Quantity to withdraw: "))
                        if (sum(itemQuant) + int(wquantity) > int(itemsBagCapacity)):
                            print()
                            print("You do not have enough bank space to do this.")
                        else:
                            wqwer = list([bankedItems[witemID - 1],])
                            wquan = list([bankedItemsQuant[witemID - 1],])
                            if (wquantity == bankedItemsQuant[witemID - 1]):
                                if (bankedItems[witemID - 1] in itemsList):
                                    tempVar = itemsList.index(bankedItems[witemID - 1])
                                    itemQuant[tempVar] = itemQuant[tempVar] + wquantity
                                    bankedItemsQuant[witemID - 1] = int(bankedItemsQuant[witemID - 1]) - wquantity
                                else:
                                    itemsList = list(itemsList) + [(bankedItems[witemID - 1]),]
                                    itemQuant = itemQuant + [wquantity]
                                    bankedItemsQuant[witemID - 1] = int(bankedItemsQuant[witemID - 1]) - wquantity
                                wtemp1 = list(bankedItems)
                                wtemp2 = list(bankedItemsQuant)
                                z = 0
                                bankedItems = []
                                bankedItemsQuant = []
                                while(z < witemID - 1):
                                    bankedItems = bankedItems + [wtemp1[z]]
                                    bankedItemsQuant = bankedItemsQuant + [wtemp2[z]]
                                    z = z + 1
                                z = witemID
                                while(z < len(wtemp1)):
                                    bankedItems = bankedItems + [wtemp1[z]]
                                    bankedItemsQuant = bankedItemsQuant + [wtemp2[z]]
                                    z = z + 1
                                z = 0
                            elif(wquantity == 0):
                                print()
                                print("You cannot move 0 of an item to your inventory.")
                                time.sleep(2)
                            elif(wquantity > bankedItemsQuant[witemID - 1]) and (wquantity > 0):
                                if (bankedItems[witemID - 1] in itemsList):
                                    tempVar = itemsList.index(bankedItems[witemID - 1])
                                    itemQuant[tempVar] = itemQuant[tempVar] + wquan
                                    bankedItemsQuant[witemID - 1] = int(bankedItemsQuant[witemID - 1]) - wquantity
                                else:
                                    itemsList = list(itemsList) + [(bankedItems[witemID - 1]),]
                                    itemQuant = itemQuant + wquan
                                    bankedItemsQuant[witemID - 1] = int(bankedItemsQuant[witemID - 1]) - wquantity
                                print("Withdrawn maximum ammount.")
                                wtemp1 = list(bankedItems)
                                wtemp2 = list(bankedItemsQuant)
                                z = 0
                                bankedItems = []
                                bankedItemsQuant = []
                                while(z < witemID - 1):
                                    bankedItems = bankedItems + [wtemp1[z]]
                                    bankedItemsQuant = bankedItemsQuant + [wtemp2[z]]
                                    z = z + 1
                                z = witemID
                                while(z < len(wtemp1)):
                                    bankedItems = bankedItems + [wtemp1[z]]
                                    bankedItemsQuant = bankedItemsQuant + [wtemp2[z]]
                                    z = z + 1
                                z = 0
                            elif(wquantity < bankedItemsQuant[witemID - 1]) and (wquantity > 0):
                                if (bankedItems[witemID - 1] in itemsList):
                                    tempVar = itemsList.index(bankedItems[witemID - 1])
                                    itemQuant[tempVar] = itemQuant[tempVar] + wquantity
                                    bankedItemsQuant[witemID - 1] = int(bankedItemsQuant[witemID - 1]) - wquantity
                                else:
                                    itemsList = list(itemsList) + [(bankedItems[witemID - 1]),]
                                    itemQuant = itemQuant + [wquantity]
                                    bankedItemsQuant[witemID - 1] = int(bankedItemsQuant[witemID - 1]) - wquantity
                elif (choice.upper() == "D"):
                    print()
                    if (len(itemsList) == 0):
                        print("Your pouch is currently empty, you cannot deposit from it.")
                        print()
                        tempVarBankDepositEmpty = input("Click Return (Enter) to coninue: ")
                    else:
                        itemID = int(input("Item to deposit: "))
                        quantity = int(input("Quantity to deposit: "))
                        if (sum(bankedItemsQuant) + int(quantity) > int(bankSize)):
                            print()
                            print("You do not have enough pouch space to do this.")
                        else:
                            qwer = list([itemsList[itemID - 1],])
                            quan = list([itemQuant[itemID - 1],])
                            if (quantity == itemQuant[itemID - 1]):
                                if (itemsList[itemID - 1] in bankedItems):
                                    tempVar = bankedItems.index(itemsList[itemID - 1])
                                    bankedItemsQuant[tempVar] = bankedItemsQuant[tempVar] + quantity
                                    itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                                else:
                                    bankedItems = list(bankedItems) + [(itemsList[itemID - 1]),]
                                    bankedItemsQuant = bankedItemsQuant + [quantity]
                                    itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                                temp1 = list(itemsList)
                                temp2 = list(itemQuant)
                                z = 0
                                itemsList = []
                                itemQuant = []
                                while(z < itemID - 1):
                                    itemsList = itemsList + [temp1[z]]
                                    itemQuant = itemQuant + [temp2[z]]
                                    z = z + 1
                                z = itemID
                                while(z < len(temp1)):
                                    itemsList = itemsList + [temp1[z]]
                                    itemQuant = itemQuant + [temp2[z]]
                                    z = z + 1
                                z = 0
                            elif(quantity == 0):#works
                                print()
                                print("You cannot move 0 of an item to your bank.")
                                time.sleep(2)
                            elif(quantity > itemQuant[itemID - 1]):#works (currently)
                                if (itemsList[itemID - 1] in bankedItems):
                                    tempVar = bankedItems.index(itemsList[itemID - 1])
                                    bankedItemsQuant[tempVar] = bankedItemsQuant[tempVar] + quan
                                    itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                                else:
                                    bankedItems = list(bankedItems) + [(itemsList[itemID - 1]),]
                                    bankedItemsQuant = bankedItemsQuant + quan
                                    itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                                print("Deposited maximum ammount.")
                                temp1 = list(itemsList)
                                temp2 = list(itemQuant)
                                z = 0
                                itemsList = []
                                itemQuant = []
                                while(z < itemID - 1):
                                    itemsList = itemsList + [temp1[z]]
                                    itemQuant = itemQuant + [temp2[z]]
                                    z = z + 1
                                z = itemID
                                while(z < len(temp1)):
                                    itemsList = itemsList + [temp1[z]]
                                    itemQuant = itemQuant + [temp2[z]]
                                    z = z + 1
                                z = 0
                            elif(quantity < itemQuant[itemID - 1]) and (quantity > 0):#works
                                if (itemsList[itemID - 1] in bankedItems):#works
                                    tempVar = bankedItems.index(itemsList[itemID - 1])
                                    bankedItemsQuant[tempVar] = bankedItemsQuant[tempVar] + quantity
                                    itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                                else:#works
                                    bankedItems = list(itemsList) + [(itemsList[itemID - 1]),]
                                    bankedItemsQuant = bankedItemsQuant + [quantity]
                                    itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                elif (choice.upper() == "C"):#Return
                    print()
                    print("~~~Bank Menu Closed~~~")
                    time.sleep(3)
                    tempVarLoop1 = 1
                else:#Error
                    print()
                    print("That is not a valid response.")


    elif (actionChoice == "3"):#Equipment
        Equipment()
    elif (actionChoice == "4"):#ExitGame
        print()
        saveGame = input("Would you like to save the game? [Y/N]: ")
        if (saveGame.upper() == "Y"):
            savedGame = open('progress.txt', 'w')
            savedGame.write("xLocation: \n")
            savedGame.write(str(xLocation))
            savedGame.write("\n")
            savedGame.write("yLocation: \n")
            savedGame.write(str(yLocation))
            savedGame.write("\n")
            savedGame.write("zLocation: \n")
            savedGame.write(str(zLocation))
            savedGame.write("\n")
            savedGame.write("location: \n")
            savedGame.write(str(location))
            savedGame.write("\n")

            savedGame.write("\n")
            savedGame.write("Current Helm: \n")
            savedGame.write(str(currentHelmType))
            savedGame.write("\n")
            savedGame.write("Current Body: \n")
            savedGame.write(str(currentBodyType))
            savedGame.write("\n")
            savedGame.write("Current Legs: \n")
            savedGame.write(str(currentLegsType))
            savedGame.write("\n")
            savedGame.write("Current Boot: \n")
            savedGame.write(str(currentBootType))
            savedGame.write("\n")

            savedGame.write("\n")
            savedGame.write("Current Weapon: \n")
            savedGame.write(str(currentWeapon))
            savedGame.write("\n")
            savedGame.write("Weapons List: \n")
            i = 0
            while (i < len(weapons)):
                savedGame.write(weapons[i])
                savedGame.write("\n")
                i = i + 1
            #Ends
            savedGame.close()
        print()
        print("       ~~~Now Exiting Game~~~")
        print()
        alive = False
    else:#Error
        print()
        print("That is not a valid response.")


##    ##    ##  See Local Mayor
##    ##    ##  get torch
##    ##    ##  Cave bats
##    ##    ##  get
##    ##    ##
##    ##    ##
##    ##    ##  BackStory:
##    ##    ##  Holy elemental temples over world, each one guarded by a sage.
##    ##    ##  Dark Lord Jeashus killed and replaced many people with his minions
##    ##    ##  he trapped the sages which became distant from one another long ago
##    ##    ##  and turned their sacred temples into his temples of darkness.
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##  Story:
##    ##    ##  first prove yourlself
##    ##    ##  then find the Lost memories of Jeashus (not where you thought they were) (each trapped in an alterate plane of existance guarded by 2 bwoss dudes at least.)
##    ##    ##      temple1 - Forest (east of square)
##    ##    ##          leads to arid badlands -
##    ##    ##      temple2 - Cave (north of square)
##    ##    ##          leads to the fields of dreams - through your journey you see rememnants of your own memories (only the happy ones)
##    ##    ##              (bwoss dude power lv is determined through the number of items which you accept in your time)
##    ##    ##                  each time you defeat the bwoss dude, he changes form
##    ##    ##      temple3 - Dwarfen Stronghold (north of mountains)
##    ##    ##          leads to eternity copse - sphynx asking questions
##    ##    ##              after getting the memory you retur to the dwarfen stronghold and find Jeashus has corrupted the dwarfs with wealth
##    ##    ##                  (bwoss batttelees is da dwarfen council)
##    ##    ##      temple4 - Sea (south-east of Isle)
##    ##    ##          leads to cloud haven - areas stood on have a chance of falling
##    ##    ##      temple5 - Mountain (north-east of square)
##    ##    ##          leads to graveyards of the damned
##    ##    ##      temple6 - Isle (south of sea)
##    ##    ##          leads to crystal kingdom -
##    ##    ##  each meemory fragment gives a new skill
##    ##    ##  ...
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##  spoiler alert: you are Jeashus
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##
##    ##    ##  when the game loads, the payers progress (in the form of their items, quests and location) are loaded from a text file
##    ##    ##  whenever the player "quit"s the game, their progress (in the form of their items, quests and location) are saved to a text file
##    ##    ##
##    ##    ##
##        https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch07s04.html
##        http://learnpythonthehardway.org/book/ex15.html
##        http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python




        """
        Single Tuple Object = ("X",)
        #Must have the comma


        itemList = ("a", "b", "c")
        item = ("d"),
        itemList = itemList + item
        itemList --> ("a", "b", "c", "d")


        """
