import random
import time
alive = True
######################################################################################################################################
#Settings
textSpeed = 1.5
######################################################################################################################################
#Location
xLocation = int(0)
yLocation = int(0)
zLocation = int(0)
locationName = ["Square", "Town Hall", "Cave Entrance", "Caves Ladder Room", "Forest Edge", "Forest", "Beach", "Sea", "Behind the Town Hall"]
location = locationName[0]
######################################################################################################################################
#Armour
armourTypes = ("Empty Slot", "Cloth", "Iron", "Steel", "Gold", "Mithril", "Alanite")
currentHelmType = 0
helmDefence = ("+0", "+1", "+2", "+4", "+6", "+9", "+13")
helmDefenceLV = (0, 1, 2, 4, 6, 9, 13)
currentBodyType = 1
bodyDefence = ("+0", "+3", "+4", "+7", "+9", "+13", "+19")
bodyDefenceLV = (0, 3, 4, 7, 9, 13, 19)
currentLegsType = 1
legsDefence = ("+0", "+1", "+2", "+4", "+6", "+9", "+16")
legsDefenceLV = (0, 1, 2, 4, 6, 9, 16)
currentBootType = 1
bootDefence = ("+0", "+1", "+2", "+4", "+6", "+9", "+13")
helmDefenceLV = (0, 1, 2, 4, 6, 9, 13)
######################################################################################################################################
#Weapons
weapons = ["Fist", "Torch", "Sword"]
currentWeapon = 0
weaponTypes = ["Melee", "Melee", "Melee"]
weaponDamages = ["+0", "+3", "+8"]
weaponDamagesLV = (0, 3, 8)
activeWeapon = ["*Equipped*", "", ""]
######################################################################################################################################
#Bag Items
    #Food

    #Armour
clothHelm = False
swimWear = False
ironBoots = False
townHallAccess = False

    #Weapons / Tools`
torch = True
    #Items
itemsList = ["stick", "stone"]
itemQuant = [4, 7]

    #Quest Items
batCorpses = 0

######################################################################################################################################
#Movement
def Movement(xLocation, yLocation, zLocation, location):
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
            else:
                print("That is not a valid response.")
                movementVar0 = 1

        elif (xLocation == -1) and (yLocation == 0) and (zLocation == 0): #TownHall
            print()
            print("What direction would you like to move in?")
            moveDirection = input("[North (N) ¦ East (E) ¦ Return (R)]: ")
            print()
            if (moveDirection.upper() == "N"):
                xLocation = xLocation + 1
                print("You have moved North behind the Town Hall")
                location = locationName[0]
                break
            elif (moveDirection.upper() == "E"):
                yLocation = yLocation + 1
                print("You have moved East back to the Square.")
                location = locationName[4]
                break
            elif (moveDirection.upper() == "R"):
                print("~~~Previous menu opened.~~~")
            else:
                print("That is not a valid response.")

        elif (xLocation == -1) and (yLocation == 1) and (zLocation == 0):  #TownHall_Behind
            print()        
            print("What direction would you like to move in?")
            moveDirection = input("[South (S) ¦ Return (R)]: ")
            print()
            if (moveDirection.upper() == "S"):
                xLocation = xLocation + 1
                print("You move South to the Town Hall entrance.")
                location = locationName[0]
                break
            elif (moveDirection.upper() == "R"):
                print("~~~Previous menu opened.~~~")
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
            else:
                print("That is not a valid response.")
                
        elif (xLocation == 0) and (yLocation == 1) and (zLocation == 0): #Caves Floor m2
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
            else:
                print("That is not a valid response.")
            print(type(xLocation))
            print(type(yLocation))
            print(type(zLocation))
            print(type(location))
        return(xLocation, yLocation, zLocation, location)
        
######################################################################################################################################
#Maps
def Location_Square():
    print()
    print("       ##########  N  ##########")
    print("       #                       #       Caves      (N)")
    print("       #                       #")
    print("       #                       #       Forest     (E)")
    print("       #                       #")
    print("                                       Sea        (S)")
    print("       W                       E")
    print("                                       Town Hall  (W)")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       ##########  S  ##########")
    print()
    return
    
def Location_Caves():
    print()
    print("       #########################")
    print("       #                       #       Square     (S)")
    print("       #                       #")
    print("       #                       #       Ladder     (D)")
    print("       #          ___          #")
    print("       #         |   |         #")
    print("       #         | L |         #")
    print("       #         |___|         #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       ##########  S  ##########")
    print()
    return
   
def Location_Caves_LadderRoom():
    print()
    print("       ########### N ###########")
    print("       #                       #       Cave Tunnels (N)")
    print("       #                       #")
    print("       #                       #       Cave River   (W)")
    print("       #          ___          #")
    print("       #         |   |                 Ladder       (U)")
    print("       #         | L |         W")
    print("       #         |___|          ")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #########################")
    print()
    return

def Location_Cave_Tunnels_1():
    print()
    print("       ##########  N  ##########")
    print("       #                       #       Deep Caves   (N)")
    print("       #                       #")
    print("       #                       #       Ladder Room  (S)")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       ##########  S  ##########")
    print()
    return
def Location_TownHall():
    print()
    print("       ##########  N  ##########")
    print("       #                       #       Back of Town Hall (N)")
    print("       #                       #")
    print("       #                       #       Town Square       (E)")
    print("       #                       #")
    print("                                       Town Hall Door    (W)")
    print("       W                       E")
    print("                                ")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #########################")
    print()
    return

def Location_TownHall_Behind():
    print()
    print("       #########################")
    print("       #                       #       Town Hall (S)")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       ##########  S  ##########")
    print()
    return

def Location_ForestEntrance():
    print()
    print("       #########################")
    print("       #                       #       Forest       (E)")
    print("       #                       #")
    print("       #                       #       Town Square  (W)")
    print("       #                       #")
    print("                                ")
    print("       W                       E")
    print("                                ")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #########################")
    print()
    return

def Location_Forest2():
    print()
    print("       ##########  N  ##########")
    print("       #                       #       Forest  (N)")
    print("       #                       #")
    print("       #                       #       Forest  (E)")
    print("       #                       #")
    print("                                       Forest  (S)")
    print("       W                       E")
    print("                                       Forest  (W)")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       #                       #")
    print("       ##########  S  ##########")
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
                        if (weaponChoice2 == 1):#SwapWeaponss
                            print()#Fill in
                            print("What weapon would you like to swap with? [1 ~", len(weapons) , "]:")
                            swapChoice = int(input("Swap Number: "))
                            if (swapChoice < len(weapons) + 1) and (swapChoice > 0): #If valid answer
                                activeWeapon[currentWeapon] = ""
                                currentWeapon = swapChoice - 1
                                activeWeapon[currentWeapon] = "*Equipped*"
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
while (alive == True):
    print()
    print("What would you like to do?")
    if (location == "Square"):
        Location_Square()
    elif (location == "Town Hall"):
        Location_TownHall()
    elif (location == "Town Hall Behind"):
        Location_TownHall()
    elif (location == "Cave Entrance"):
        Location_TownHall()
    elif (location == "Caves Ladder Room"):
        Location_TownHall()
    elif (location == "Forest Edge"):
        Location_TownHall()
    elif (location == "Forest Edge"):
        Location_TownHall()
    elif (location == "Forest"):
        Location_TownHall()
    elif (location == "Beach"):
        Location_TownHall()
    elif (location == "Sea"):
        Location_TownHall()
    elif (location == "Behind the Town Hall"):
        Location_TownHall_Behind()
    else:
        print()
    actionChoice = input("  [Move (1) ¦ Inspect (2) ¦ Equipment (3)]: ")
    if (actionChoice == "1"):#Move
#https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch07s04.html
        (xLocation, yLocation, zLocation, location) = Movement(xLocation, yLocation, zLocation, location)
        print(xLocation)
        print(yLocation)
        print(zLocation)
        print(location)
        print()
    elif (actionChoice == "2"):#Inspect
        print()
    elif (actionChoice == "3"):#Equipment
        Equipment()
    else:#Error
        print()
        print("That is not a valid response.")














    
