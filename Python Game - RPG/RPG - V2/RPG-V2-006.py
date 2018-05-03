import random
import time
#print("TODO LIST:")
#print("----------")
#print()
#print("█ 1. Add current Map upgrades to Move Option")
#print("█ 2. Add Inspect option for Seafront item stalls.")
#print("█ 3. Add option for Inspect to choose between [Look Around ¦ Use Item ¦ Speak to Person]")
#print("█ 4. Add Eat Food options for food pouch (remove max food carrying limit and add food too items pouch).")
#print("█ 5. Replace numeric Return key with ("R").")
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
locationName = ["Square", "Town Hall", "Cave Entrance", "Caves Ladder Room", "Forest Entrance", "Forest", "Beach", "Sea", "Town Bank", "Cave Tunnels Entrance", "Coast", "Deep Tunnels", "Seafront Shops", "Oceanic Bridge", "Underground River", "TempForest (N)", "Deep Forest", "Western Swampland", "Oceanic Bridge Crossing", "Seafront Coast", "Broken Oceanic Bridge", "Western Deep Waters", "Beach End", "Oceanic Bridge Sea Ramp", "Rocky Coast", "Far Western Deepwaters", "Field Plains", "Forest Village", "Dark Forest Chasm", "Oceanic Bridge Split", "Swamplands", "Eastern Swamplands"]
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
clothHelm = False
swimWear = True
ironBoots = False
townHallAccess = True
torch = True

    #Items
itemsBagCapacity = 30
itemsList = ["Stick ", "Stone "]
itemQuant = [4, 5]

    #Potion Pouch
potionPouch = ["Strength Potion    ",]
potionQuant = [2,]

    #Food Pouch
foodPouch = ["Fish Pie         ","Glowing Lobster  ",]
foodQuant = [5,1]

    #Potion Stall - SeafrontShops
sfsPotionShopItems = ["Health Boost Potion", "Strength Potion    ", "Hostile Mob Repel  "]
sfsPotionShopPrices = [30, 20, 15]

    #Food Stall - SeafrontShops
sfsFoodShopItems = ["Lobster          ", "Fish Pie         ", "Glowing Lobster  "]
sfsFoodShopPrices = [30, 25, 70]

    #Bank
bankSize = 150
bankedItems = ["Bread ","Pie   ","Butter",]
bankedItemsQuant = [6,4,3]

    #Wealth
mS = "§"
moneyPouch = 100

######################################################################################################################################
    #Entities
creatureHealth = 0
creatureDamage = 0
creatureAttackEXP = 0
creatureDamageEXP = 0

#####################
#Bat
batHealth = 100
batDamage = 5
batAttackExp = 1
batDefenceExp = 1
#####################



######################################################################################################################################
#Bank
#def bank(itemsList, itemQuant, itemsBagCapacity, bankedItems, bankedItemsQuant, bankSize):

######################################################################################################################################
#Inspection

def objectInspection():
    if (object == "Hostile_Bat"):
        print ("█ This bat looks like it might attack you...")



######################################################################################################################################
#General Fight

def mobstats():
    if (mob == bat):
        creatureHealth = batHealth
        creatureDamage = batDamage
def generalFight():

    print("█ What would you like to do?")
    decision = input("█ [Fight (1) ¦ Use Item (2)¦ Run (3)]: ")
    print ("█")
    
    mobstats()
    while(decision == 3):
        print("You run away from the creature.")
        break
    if(decision == 1):
        maxHealth = defenceLevel + weaponDefence + 20
        ownHealth = maxHealth
    while (decision.lower() == "leftclick"):
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
            dropPercentage = int(random.random() * 10 )
            if (dropPercentage > 4):
                batCorpse = batCorpse + 1
                print("The number of Bat Corpses you now have is: ", batCorpse)
            print ("Another bat comes out of the darkness, would you like to attack it?")
            print ("Leftclick to Fight | Rightclick to Leave")
            decision = input()    
            if(decision.lower() == "rightclick"):
                print("Return to your adventure another day!")
                break
            creatureHealth = 100
        return

######################################################################################################################################
#Mob Introductions
    
def batIntro():
    print ("You encounter a Hostile Bat.")
    time.sleep(1)
    print ("It flies past you.")
    time.sleep(1)
    print ("Would you like to inspect the Hostile Bat?")

    inspection = input("(Y/N):  ")
    if (inspection.upper() == "Y"):
        objectInspection()

    print()
    print ("The Hostile Bat comes back towards you.")


######################################################################################################################################
#Maps
def Location_Square():
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██                     ██       Caves      (N)")
    print("█        ██                     ██ ")
    print("█        ██       ▄     ▄       ██       Forest     (E)")
    print("█       ▀▀▀     ▄▄█     █▄▄     ▀▀▀")
    print("█                                        Beach      (S)")
    print("█        W                       E ")
    print("█                                        Town Hall  (W)")
    print("█       ▄▄▄     ▀▀█     █▀▀     ▄▄▄")
    print("█        ██       ▀     ▀       ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████   S   █████████ ")
    print("█                ▀       ▀         ")
    return

def Location_Caves():
    print("█")
    print("█        █████████████████████████ ")
    print("█        ██                     ██       Square     (S)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Ladder     (D)")
    print("█        ██                     ██ ")
    print("█        ██        ╔═══╗        ██ ")
    print("█        ██        ║ L ║        ██ ")
    print("█        ██        ╚═══╝        ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████   S   █████████ ")
    print("█                ▀       ▀         ")
    return

def Location_Caves_LadderRoom():
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██                     ██       Cave Tunnels (N)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Cave River   (E)")
    print("█        ██                     ▀▀▀")
    print("█        ██        ┌───┐                 Ladder       (U)")
    print("█        ██        │ L │         E ")
    print("█        ██        └───┘           ")
    print("█        ██                     ▄▄▄")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████████████████████ ")
    print("█")
    return

def Location_Underground_River():
    print("█                ▄       ▄         ")
    print("█        ██████████  N  ██████████ ")
    print("█        ██       │-----│       ██       Northern Underground River (N)")
    print("█        ██       │-----└─┐     ██ ")
    print("█        ██       │-------└─┐   ██       Southern Underground River (E)")
    print("█       ▀▀▀       └┐--------└───██▀")
    print("█                  │------------         Ladder Room                (W)")
    print("█        W         └┐----------- E ")
    print("█                   └──┐--------   ")
    print("█       ▄▄▄            └────────██▄")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████████████████████ ")
    print("█")
    return

def Location_Cave_Tunnels_1():
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██                     ██       Deep Caves   (N)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Ladder Room  (S)")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████   S   █████████ ")
    print("█                ▀       ▀         ")
    return

def Location_Town_Bank():
    print("█")
    print("█   Use [Inspect (2)] to access the bank.")
    print("█               ▄▄▄▄▄▄▄▄▄▄▄         ")
    print("█        ████████         ████████ ")
    print("█        ██     █  § § §  █     ██       Town Hall   (S)")
    print("█        ██     █         █     ██ ")
    print("█        ██     ▀▀▀     ▀▀▀     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████   S   █████████ ")
    print("█                ▀       ▀         ")
    return

def Location_TownHall():
    print("█")
    print("█   Use [Inspect (2)] to enter the Town Hall.")
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██                     ██       Bank           (N)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Town Square    (E)")
    print("█       █▀▀▀▀▀█                 ▀▀▀")
    print("█       █     ▀                          Seafront Shops (S)")
    print("█       █                        E ")
    print("█       █     ▄                    ")
    print("█       █▄▄▄▄▄█                 ▄▄▄")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████   S   █████████ ")
    print("█                ▀       ▀         ")
    return

def Location_ForestEntrance():
    print("█")
    print("█        █████████████████████████ ")
    print("█        ██                     ██       Forest       (E)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Town Square  (W)")
    print("█       ▀▀▀                     ▀▀▀")
    print("█                                  ")
    print("█        W                       E ")
    print("█                                  ")
    print("█       ▄▄▄                     ▄▄▄")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████████████████████ ")
    print("█")
    return

def Location_Forest():
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██                     ██       Forest             (N)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Deep Forest        (E)")
    print("█       ▀▀▀                     ▀▀▀")
    print("█                                        Western Swamplands (S)")
    print("█        W                       E ")
    print("█                                        Forest Entrance    (W)")
    print("█       ▄▄▄                     ▄▄▄")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████   S   █████████ ")
    print("█                ▀       ▀         ")
    return

def Location_Deep_Forest():
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██                     ██       Forest Village    (N)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Dark Forest Chasm (E)")
    print("█       ▀▀▀                     ▀▀▀")
    print("█                                        Forest            (W)")
    print("█        W                       E ")
    print("█                                  ")
    print("█       ▄▄▄                     ▄▄▄")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        ██                     ██ ")
    print("█        █████████████████████████ ")
    print("█")
    return

def Location_Western_Swamplands():
    print("█                ▄       ▄         ")
    print("█        ██████████  N  ██████████ ")
    print("█        ██               ┌┘------       Forest     (N)")
    print("█        ██      ┌─┤ ├────┘------- ")
    print("█        ██──────┘-│ │-----------┌       Swamplands (E)")
    print("█        ██--------│ │----------┌┘ ")
    print("█        ██----┌───┤ ├┐--------┌┘  ")
    print("█        ██--┌─┘      │--------│ E ")
    print("█        ██--│       ┌┘--------└┐  ")
    print("█        ██--│       ┴──────────┴  ")
    print("█        ██-┌┘       ┬──────────┬  ")
    print("█        ██─┘       ┌┘--------┌─┘  ")
    print("█        ██         │--------┌┘    ")
    print("█        █████████████████████████ ")
    print("█")
    return

def Location_Swamplands():
    print("█")
    print("█        █████████████████████████ ")
    print("█        --------│         │------       Eastern SwampLands (E)")
    print("█        -┌──┐---└─┐       │------ ")
    print("█        ─┘  ┴─────┴      ┌┘------       Western SwampLands (W)")
    print("█             ┬─────┬     │------- ")
    print("█             │-----└┐   ┌┘-----   ")
    print("█        W   ┌┘------└┤ ├┘------ E ")
    print("█           ┌┘--------│ │-------   ")
    print("█           │---------│ │-----┌─── ")
    print("█           │---------│ │┌────┘    ")
    print("█          ┌┘--------┌┤ ├┘         ")
    print("█          │-------┌─┘             ")
    print("█        █████████████████████████ ")
    print("█")
    return

def Location_Eastern_Swamplands():
    print("█")
    print("█        █████████████████████████ ")
    print("█        ---│                   ██      SwampLands          (W)")
    print("█        ---└┐  D  ┌──────┐     ██ ")
    print("█        ----└─────┘------└┐    ██      Enter Swamp Dungeon (D)")
    print("█        ------------------│    ██ ")
    print("█        ------------------│    ██ ")
    print("█        -----------------┌┘    ██ ")
    print("█        -----------------│     ██ ")
    print("█       ──┐--------------┌┘     ██ ")
    print("█         └────┐-------┌-┘      ██ ")
    print("█              └───────┘        ██ ")
    print("█                               ██ ")
    print("█        █████████████████████████ ")
    print("█")
    return

def Location_Oceanic_Bridge():
    print("█")
    print("█        █████████████████████████ ")
    print("█        ██                     ██       Oceanic Island Bridge (S)")#which will be blocked! mwahahaaa & will look like PkMon bridge where you find snorlax
    print("█        ██                     ██ ")
    print("█        ██                     ██       Beach                 (W)")
    print("█       ▀▀▀                     ██ ")
    print("█                               ██ ")
    print("█        W                      ██ ")
    print("█                               ██ ")
    print("█        -----------------│   │-██ ")
    print("█        -----------------│   │-██ ")
    print("█        -----------------│   │-██ ")
    print("█        -----------------│   │-██ ")
    print("█        ---------   S   -│   │-██ ")
    print("█")
    return

def Location_Oceanic_Bridge_Crossing():
    print("█")
    print("█        ---------   N   -│   │-██ ")
    print("█        -----------------│   │---       Oceanic Bridge Start       (N)")
    print("█        ----┌────────────┘   │--- ")
    print("█        ----│                │---       Oceanic Bridge Sea Ramp    (E)")
    print("█        ----│   ┌────────────┘--- ")
    print("█          --│   │--------------         Broken Oceanic Bridge Path (S)")
    print("█        W --│   └─────────┐---- E ")
    print("█          --│             │----         Coast                      (W)")
    print("█        ----│   ┌─────┐   └────── ")
    print("█        ----│ X │-----│           ")
    print("█        ----│X █│-----└────────── ")
    print("█        ====│█XX│================ ")
    print("█        ====│X X│=  S  ========== ")
    print("█")
    return

def Location_Oceanic_Bridge_Ramp():
    print("█")
    print("█        ██████████████████████████ ")
    print("█        --------------------------      Oceanic Bridge Split       (E)")
    print("█        ------------------------- ")
    print("█        ----------┌──────────────       Oceanic Tidal Currents     (S)") #takes you to the beach end and deals damage
    print("█        --------╔─┘               ")
    print("█          ------║     ┌──────────       Oceanic Bridge Crossing    (W)")
    print("█        W ------╚─┐   │-------- E ")
    print("█          --------│   │--------   ")
    print("█        ──────────┘   │---------- ")
    print("█                      │---------- ")
    print("█        ──────────────┘---------- ")
    print("█        ========================= ")
    print("█        ==========  S  ========== ")
    print("█")
    return

def Location_Broken_Oceanic_Bridge():
    print("█")
    print("█        ####│X X│#  N  ########## ")
    print("█        ####│X  │################       Oceanic Bridge Crossing (N)")
    print("█        ####│ X█│################ ")
    print("█        ####│█ X│################       Oceanic Island Shallows (E)")
    print("█        ####│XX │################ ")
    print("█          ##│██X└##############        Southern Deepwaters     (S)")
    print("█        W ##│XX ############### E ")
    print("█          ##└##################        Eastern Deepwaters      (W)")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ##########  S  ########## ")
    print("█")
    return

def Location_Beach():
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██                     ██       Square          (N)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Oceanic Bridge  (E)")
    print("█       ▀▀▀                     ▀▀▀")
    print("█                                        Sea             (S)")
    print("█        W                       E ")
    print("█                                        Seafront Shops  (W)")
    print("█        ------------------------- ")
    print("█        ------------------------- ")
    print("█        ------------------------- ")
    print("█        ------------------------- ")
    print("█        ----------  S  ---------- ")
    print("█")
    return

def Location_Seafront_Shops():
    print("█")
    print("█   Use [Inspect (2)] to choose a shop to enter.")
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██      ║       ║      ██       Town Hall    (N)")
    print("█        ██══════╝       ╚══════██ ")
    print("█        ██                     ██       Beach        (E)")
    print("█       ▀▀▀                     ▀▀▀")
    print("█                                        Sea          (S)")
    print("█        W                       E ")
    print("█                                        Beach End    (W)")
    print("█        ------------------------- ")
    print("█        ------------------------- ")
    print("█        ------------------------- ")
    print("█        ------------------------- ")
    print("█        ----------  S  ---------- ")
    print("█")
    return

def Location_Beach_End():
    print("█                ▄       ▄         ")
    print("█        █████████   N   █████████ ")
    print("█        ██                     ██       Field Plains   (N)")
    print("█        ██                     ██ ")
    print("█        ██                     ██       Seafront Shops (E)")
    print("█        ██                     ▀▀▀")
    print("█        ██                              Rocky Coast    (S)")
    print("█        ██                      E ")
    print("█        ██                        ")
    print("█        ██----------------------- ")
    print("█        ██----------------------- ")
    print("█        ██----------------------- ")
    print("█        ██----------------------- ")
    print("█        ██--------  S  ---------- ")
    print("█")
    return

def Location_Rocky_Coast():
    print("█")
    print("█        ██--¤-----  N  -------¤-- ")
    print("█        ██-------¤---¤---¤-------       Beach End              (N)")
    print("█        ██¤---¤---¤---¤¤-----¤--- ")
    print("█        ██---¤--¤----¤------¤----       Seafront Coast         (E)")
    print("█        ██-¤-----¤------¤-------- ")
    print("█        ██----¤----¤---¤----¤--         Far Western Deepwaters (S)")
    print("█        ██-----¤-----¤----¤---- E ")
    print("█        ██-------¤¤---¤--------   ")
    print("█        ██---¤----¤-¤------¤----- ")
    print("█        ██-¤----------¤--------¤- ")
    print("█        ██------¤------¤-----¤--- ")
    print("█        ██=====¤=========¤===¤=== ")
    print("█        ██¤=======  S  ========== ")
    print("█")
    return

def Location_Far_Western_DeepWaters():
    print("█")
    print("█        ██########  N  ########## ")
    print("█        ██#######################        Rocky Coast         (N)")
    print("█        ██####################### ")
    print("█        ██#######################        Western Deep Waters (E)")
    print("█        ██####################### ")
    print("█        ██#####################          Southern Deepwaters (S)")
    print("█        ██##################### E ")
    print("█        ██#####################   ")
    print("█        ██####################### ")
    print("█        ██####################### ")
    print("█        ██####################### ")
    print("█        ██####################### ")
    print("█        ██########  S  ########## ")
    print("█")
    return

def Location_Seafront_Coast():
    print("█")
    print("█        ----------  N  ---------- ")
    print("█        -------------------------       Seafront Shops      (N)")
    print("█        ------------------------- ")
    print("█        -------------------------       Coast               (E)")
    print("█        ------------------------- ")
    print("█          ---------------------         Western Deep Waters (S)")
    print("█        W --------------------- E ")
    print("█          ---------------------         Rocky Coast         (W)")
    print("█        ------------------------- ")
    print("█        ------------------------- ")
    print("█        ------------------------- ")
    print("█        ========================= ")
    print("█        ==========  S  ========== ")
    print("█")
    return

def Location_Sea():
    print("█")
    print("█        ##########  N  ########## ")
    print("█        #########################       Coast              (N)")
    print("█        ######################### ")
    print("█        #########################       Broken Oceanic Bridge Path (E)")
    print("█        ######################### ")
    print("█          #####################         Southern Deepwaters        (S)")
    print("█        W ##################### E ")
    print("█          #####################         Western Deepwaters         (W)")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ##########  S  ########## ")
    print("█")
    return

def Location_Western_DeepWaters():
    print("█")
    print("█        ##########  N  ########## ")
    print("█        #########################        Seafront Coast         (N)")
    print("█        ######################### ")
    print("█        #########################        Deep Sea               (E)")
    print("█        ######################### ")
    print("█          #####################          Southern Deepwaters    (S)")
    print("█        W ##################### E ")
    print("█          #####################          Far Western Deepwaters (W)")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ######################### ")
    print("█        ##########  S  ########## ")
    print("█")
    return


######################################################################################################################################
#Equipment
##def Equipment():
##    currentWeapon = 0
##    equipmentVar = 0
##    while(equipmentVar == 0):
##        print("█")
##        print("█   Equipment Options:")
##        print("█   Current Wealth: ", mS, moneyPouch)
##        equipmentChoice1 = int(input("█ [View Armour (1) ¦ View Weapons (2) ¦ View Bag (3) ¦ Eat Food (4) ¦ Return (5)]: "))
##        if (equipmentChoice1 == 1): #ViewArmour
##            print("█")
##            print("█ Helm:   ",armourTypes[currentHelmType])
##            print("█ Body:   ",armourTypes[currentBodyType])
##            print("█ Legs:   ",armourTypes[currentLegsType])
##            print("█ Boot:   ",armourTypes[currentBootType])
##            equipmentVar2 = 0
##            while(equipmentVar2 == 0):
##                print("█")
##                print("█")
##                print("█")
##                print("█ More Information:")
##                armourChoice1 = int(input("█ [Helm Stats (1) ¦ Body Stats (2) ¦ Legs Stats (3) ¦ Boot Stats (4) ¦ Return (5)]: "))
##                if(armourChoice1 == 1):
##                    print("█")
##                    print("█ Helm  Type: ",armourTypes[currentHelmType])
##                    print("█ Helm Defence: ",helmDefence[currentHelmType])
##                elif (armourChoice1 == 2):
##                    print("█")
##                    print("█ Body Type: ",armourTypes[currentBodyType])
##                    print("█ Body Defence: ",helmDefence[currentBodyType])
##                elif (armourChoice1 == 3):
##                    print("█")
##                    print("█ Legs Type: ",armourTypes[currentLegsType])
##                    print("█ Legs Defence: ",legsDefence[currentLegsType])
##                elif (armourChoice1 == 4):
##                    print("█")
##                    print("█ Boot Type: ",armourTypes[currentBootType])
##                    print("█ Boot Defence: ",bootDefence[currentBootType])
##                elif (armourChoice1 == 5):
##                    print("█")
##                    print("█ ~~~Previous menu opened.~~~")
##                    equipmentVar2 = 1
##                else:
##                    print("█")
##                    print("█ That is not a valid response.")
##        elif (equipmentChoice1 == 2):#ViewWeapons
##            while (equipmentChoice1 == 2):
##                print("█")
##                print("█")
##                print("█ Current Weapon:    ", weapons[currentWeapon])
##                print("█")
##                print("█ Weapon Options:")
##                weaponChoice1 = int(input("█ [List Weapons (1) ¦ Get Weapon Stats (2) ¦ Return (3)]: "))
##                if (weaponChoice1 == 1):#ListWeapons
##                    print("█")
##                    print("█ Owned Weapons:")
##                    weaponslist = int(0)
##                    while (weaponslist < len(weapons)):
##                        print("█ ",(weaponslist + 1), "): ", weapons[weaponslist], "    ", activeWeapon[weaponslist])
##                        weaponslist = weaponslist + 1
##                    print("█")
##                    weaponChoiceVar2 = 0
##                    while(weaponChoiceVar2 == 0):
##                        print("█ Weapon Choices: ")
##                        weaponChoice2 = int(input("█ [Swap Weapons (1)¦ Return (2)]: "))
##                        if (weaponChoice2 == 1):#SwapWeapons
##                            print("█")#Fill in
##                            print("█ What weapon would you like to swap with? [1 ~", len(weapons) , "]:")
##                            swapChoice = int(input("█ Swap Number: "))
##                            if (swapChoice < len(weapons) + 1) and (swapChoice > 0): #If valid answer
##                                activeWeapon[currentWeapon] = ""
##                                currentWeapon = swapChoice - 1
##                                activeWeapon[currentWeapon] = "*Equipped*"
##                                print("█")
##                                print("█ These are the statistics for your now equipped weapon.")
##                                print("█ Weapon: ", weapons[currentWeapon])
##                                print("█ Type:   ", weaponTypes[currentWeapon])
##                                print("█ Damage: ", weaponDamages[currentWeapon])
##                            else:#Error
##                                print("█")
##                                print("█ That is not a valid response.")
##                            weaponChoiceVar2 = 1
##                        elif (weaponChoice2 == 2):#Return
##                            print("█")
##                            print("█ ~~~Previous menu opened.~~~")
##                            weaponChoiceVar2 = 1
##                            equipmentChoice1 = 0
##                        else:#Error
##                            print("█")
##                            print("█ That is not a valid response.")
##                            weaponChoiceVar2 = 1
##
##                    equipmentChoice1 = 0
##                elif (weaponChoice1 == 2):#GetWeaponStats
##                    print("█")
##                    print("█ These are the statistics for your current weapon.")
##                    print("█ Weapon: ", weapons[currentWeapon])
##                    print("█ Type:   ", weaponTypes[currentWeapon])
##                    print("█ Damage: ", weaponDamages[currentWeapon])
##                    equipmentChoice1 = 0
##                elif (weaponChoice1 == 3):#Return
##                    print("█")
##                    print("█ ~~~Previous menu opened.~~~")
##                    equipmentChoice1 = 0
##                else:#Error
##                    print("█")
##                    print("█ That is not a valid response.")
##        elif (equipmentChoice1 == 3):#ViewBag
##            print("█")
##            bagVar1 = 0
##            while(bagVar1 == 0):
##                print("█ What pouch would you like to view: ")
##                bagChoice = int(input("█ [Items (1) ¦ Quest Items (2) ¦ Return (3)]: "))
##                if(bagChoice == 1):#Items
##                    print("█")
##                    print("█ Pouch Items:")
##                    itemsListVar1 = int(0)
##                    while (itemsListVar1 < len(itemsList)):
##                        print("█ ",(itemsListVar1 + 1), ") ", itemsList[itemsListVar1], "    ->    ", itemQuant[itemsListVar1])
##                        itemsListVar1 = itemsListVar1 + 1
##                    print("█")
##                    print("█ Pouch Quantity: ", sum(itemQuant), " /50")   #INC Custom Bag Pouches
##                    itemChoiceVar = 0
##                    while(itemChoiceVar == 0):
##                        print("█ What would you like to do: ")
##                        itemChoiceVar2 = int(input("█ [Drop Item (1) ¦ Use Item (2) ¦ Inspect (3) ¦ Return (4)]: "))
##                        print("█")
##                        if(itemChoiceVar2 == 1):#DropItem
##                            print("█ What item would you like to drop? [ 0 ~", len(itemsList), "]:")
##                            itemDropID = int(input("█ Item ID to Drop: "))
##                            if(itemDropID < len(weapons) + 1) and (itemDropID > 0): #If valid answer)
##                                itemDropQuantVar = 0
##                                while(itemDropQuantVar == 0):
##                                    print("█")
##                                    print("█ How many of", itemsList[itemDropID - 1], "would you like to drop? [0 ~", itemQuant[itemDropID - 1], "]:")
##                                    itemDropQuant = int(input("█ Number of items to drop: "))
##                                    if(itemDropQuant <= itemQuant[itemDropID - 1]) and (itemDropQuant >= 0):
##                                        if (itemDropQuant == 0):
##                                            print("█")
##                                            print("█ You have dropped nothing.")
##                                            itemDropQuantVar = 1
##                                        else:
##                                            itemQuant[itemDropID - 1] = itemQuant[itemDropID - 1] - itemDropQuant
##                                            itemDropQuantVar = 1
##                                            print("█")
##                                            print("█ You have dropped", itemDropQuant, "of", itemsList[itemDropID - 1])
##                                            print("█ You have", itemQuant[itemDropID - 1], "remaining.")
##                                            print("█")
##                                    else: #Error
##                                        print("█")
##                                        print("█ That is not a valid response.")
##                                    if(itemQuant[itemDropID - 1] == 0):
##                                        temp1 = list(itemsList)
##                                        temp2 = list(itemQuant)
##                                        z = 0
##                                        itemsList = []
##                                        itemQuant = []
##                                        while(z < itemID - 1):
##                                            itemsList = itemsList + [temp1[z]]
##                                            itemQuant = itemQuant + [temp2[z]]
##                                            z = z + 1
##                                        z = itemID
##                                        while(z < len(temp1)):
##                                            itemsList = itemsList + [temp1[z]]
##                                            itemQuant = itemQuant + [temp2[z]]
##                                            z = z + 1
##                                        z = 0
##
##
##
##
##
##
##
##
##
##
##
##                                        #######################################################################################################################################################################
##                            else:#Error
##                                print("█")
##                                print("█ That is not a valid response.")
##
##                        elif(itemChoiceVar2 == 2):#UseItem
##                            ...
##                        elif(itemChoiceVar2 == 3):#Inspect
##                            ...
##                        elif(itemChoiceVar2 == 4):#Return
##                            print("█")
##                            print("█ ~~~Previous menu opened.~~~")
##                            itemChoiceVar = 1
##                        else:#Error
##                            print("█")
##                            print("█ That is not a valid response.")
##                    print("█")
##                elif(bagChoice == 2):#QuestItems
##                    print("█")
##                elif(bagChoice == 3):#Return
##                    print("█")
##                    print("█")
##                    print("█ ~~~Previous menu opened.~~~")
##                    bagVar1 = 1
##                else:#Error
##                    print("█")
##                    print("█ That is not a valid response.")
##        elif (equipmentChoice1 == 4):#Eat Food
##            print("█")
##            print("█ ~~~Previous menu opened.~~~")
##            equipmentVar = 1
##        elif (equipmentChoice1 == 5):#Return
##            print("█")
##            print("█ ~~~Previous menu opened.~~~")
##            equipmentVar = 1
##        else:#Error
##            print("█")
##            print("█ That is not a valid response.")
##    return


######################################################################################################################################
#Actions
print("█   What is your name?")
name = input("█   Name: ")
spac = len(name) * " "

alive = True
while (alive == True):
    print("█")
    print("█   What would you like to do?")
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
    elif (xLocation == 0) and (yLocation == 2) and (zLocation == -1):#6
        Location_Cave_Tunnels_1()
    elif (xLocation == 1) and (yLocation == 0) and (zLocation == 0):
        Location_Forest_Entrance()
    elif (xLocation == 2) and (yLocation == 0) and (zLocation == 0):
        Location_Forest()
    elif (xLocation == 0) and (yLocation == -1) and (zLocation == 0):
        Location_Beach()
    elif (xLocation == 0) and (yLocation == -1) and (zLocation == 0):
        Location_Coast()
    elif (xLocation == 0) and (yLocation == -3) and (zLocation == 0):
        Location_Sea()
    elif (xLocation == -1) and (yLocation == -1) and (zLocation == 0):
        Location_Seafront_Shops()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Oceanic_Bridge()


    elif (xLocation == 1) and (yLocation == -1) and (zLocation == -1):
        Location_Underground_River()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_TempForest()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Deep_Forest()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Western_Swamplands()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Oceanic_Bridge_Crossing()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Seafront_Coast()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Oceanic_Bridge()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Broken_Oceanic_Bridge()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Western_DeepWaters()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Beach_End()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Oceanic_Bridge_Ramp()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Rocky_Coast
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Far_Western_DeepWaters()


    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Field_Plains()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_ForestVillage()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Dark_Forest_Chasm()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Oceanic_Bridge_Split()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Swamplands()
    elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0):
        Location_Eastern_Swamplands()


    else:
        print("█")

    actionChoice = input("█   [Move (1) ¦ Inspect (2) ¦ Equipment (3) ¦ Exit Game (4)]: ")
    if (actionChoice == "1"):#Move
        movementVar0 = 0
        while(movementVar0 == 0):
            if ((xLocation == 0) and (yLocation == 0) and (zLocation == 0)): #Square
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ South (S) ¦ East (E) ¦ West(W) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    if (torch == True):
                        yLocation = yLocation + 1
                        print("█   You have moved North to the Cave Entrance")
                        location = locationName[2]
                        break
                    else:
                        print("█   You need a light source to go into those caves.")
                elif (moveDirection.upper() == "S"):
                    if (swimWear == True):
                        yLocation = yLocation - 1
                        print("█   You have moved South to the Beach")
                        location = locationName[6]
                        break
                    else:
                        print("█   That water looks too cold to swim in this time of year.")
                elif (moveDirection.upper() == "E"):
                    if (ironBoots == True):
                        xLocation = xLocation + 1
                        print("█   You have moved East to the Forest Entrance.")
                        location = locationName[4]
                        break
                    else:
                        print("█   You need some stronger boots to go in there.")
                elif (moveDirection.upper() == "W"):
                    xLocation = xLocation - 1
                    print("█   You have moved west towards the Town Hall.")
                    location = locationName[1]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")

            elif (xLocation == -1) and (yLocation == 0) and (zLocation == 0): #TownHall
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ East (E) ¦ South (S) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("█   You have moved North to the Town Bank")
                    location = locationName[8]
                    break
                elif (moveDirection.upper() == "E"):
                    xLocation = xLocation + 1
                    print("█   You have moved East back to the Square.")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("█   You have moved South to the Seafront Shops.")
                    location = locationName[12]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")

            elif (xLocation == -1) and (yLocation == 1) and (zLocation == 0):  #Town_Bank
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [South (S) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("█   You move South to the Town Hall.")
                    location = locationName[1]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")

            elif (xLocation == 0) and (yLocation == 1) and (zLocation == 0): #Cave Entrance
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [South (S) ¦ Climb down Ladder (D) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("█ You move South back to the Square.")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "D"):
                    zLocation = zLocation - 1
                    print("█ You climb down the ladder to a lower floor in the cave.")
                    location = locationName[3]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")

            elif (xLocation == 0) and (yLocation == 1) and (zLocation == -1): #Caves Floor LadderRoom
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ Climb up Ladder (U) ¦ East (E) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation - 1
                    print("█   You move North further into the Cave Tunnels.")
                    location = locationName[11]
                    break
                elif (moveDirection.upper() == "U"):
                    zLocation = zLocation - 1
                    print("█   You climb up the ladder to the Cave Entrance.")
                    location = locationName[2]
                    break
                elif (moveDirection.upper() == "E"):
                    zLocation = zLocation - 1
                    print("█   You move out of the cave arriving at a river.")
                    location = locationName[14]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")

            elif (xLocation == 0) and (yLocation == 2) and (zLocation == -1): #Cave Tunnels
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ South (S) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("█   You move further into the tunnels.")
                    location = locationName[11]
                    break
                elif (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("█   You move South making your way back to the room with the Ladder.")
                    location = locationName[3]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")

            elif (xLocation == 1) and (yLocation == 0) and (zLocation == -1): #Forest Entrance
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [East (E) ¦ West (W) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "E"):
                    xLocation = xLocation + 1
                    print("█   You move deeper into the forest.")
                    location = locationName[5]
                    break
                elif (moveDirection.upper() == "W"):
                    xLocation = xLocation - 1
                    print("█   You move back to the Town Square.")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")
            elif (xLocation == 2) and (yLocation == 0) and (zLocation == 0): #Deep Forest
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ East (E) ¦ South (S) ¦ West (W) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("█   You climb through the forest.")
                    location = locationName[15]
                    break
                elif (moveDirection.upper() == "E"):
                    xLocation = xLocation + 1
                    print("█   You climb even deeper into the forest.")
                    location = locationName[16]
                    break
                elif (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("█   You climb through the forest and reach a swamp.")
                    location = locationName[17]
                    break
                elif (moveDirection.upper() == "W"):
                    xLocation = xLocation - 1
                    print("█   You move back towards the Town Square.")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")
            elif (xLocation == 0) and (yLocation == -1) and (zLocation == 0): #Beach
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ East (E) ¦ South (S) ¦ West (W) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("█   You move back towards the Town Square.")
                    location = locationName[0]
                    break
                elif (moveDirection.upper() == "E"):
                    xLocation = xLocation + 1
                    print("█    You walk along the sandy beach to a bridge.")
                    location = locationName[13]
                    break
                elif (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("█   You swim out to the edge of the coast.")
                    location = locationName[10]
                    break
                elif (moveDirection.upper() == "W"):
                    xLocation = xLocation - 1
                    print("█   You walk along the sandy beach to a row of Seafront Shops. ")
                    location = locationName[12]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")
            elif (xLocation == 0) and (yLocation == -2) and (zLocation == 0): #Coast
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ East (E) ¦ South (S) ¦ West (W) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("█   You swim to the nearby beach.")
                    location = locationName[6]
                    break
                elif (moveDirection.upper() == "E"):
                    xLocation = xLocation + 1
                    print("█   You swim up to the sea bridge.")
                    location = locationName[18]
                    break
                elif (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("█   You swim out to deeper waters.")
                    location = locationName[7]
                    break
                elif (moveDirection.upper() == "W"):
                    xLocation = xLocation - 1
                    print("█   You swim along the shoreline. ")
                    location = locationName[19]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")
            elif (xLocation == 0) and (yLocation == -3) and (zLocation == 0): #Sea
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ East (E) ¦ South (S) ¦ West (W) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("█   You swim into shallow waters.")
                    location = locationName[10]
                    break
                elif (moveDirection.upper() == "E"):
                    xLocation = xLocation + 1
                    print("█    You swim East towards an island in the distance but stop at a broken oceanic bridge.")#Me No Likey
                    location = locationName[20]
                    break
                elif (moveDirection.upper() == "S"):
                    yLocation = yLocation
                    print("█   You swim out to deeper waters but get cought in a current and get sent back.")
                    location = locationName[7]
                    break
                elif (moveDirection.upper() == "W"):
                    xLocation = xLocation - 1
                    print("█   You swim through the deeper waters to the West. ")
                    location = locationName[21]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")
            elif (xLocation == -1) and (yLocation == -1) and (zLocation == 0): #Seafront Shops
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [North (N) ¦ East (E) ¦ South (S) ¦ West (W) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "N"):
                    yLocation = yLocation + 1
                    print("█   You head towards the Town Hall.")
                    location = locationName[1]
                    break
                elif (moveDirection.upper() == "E"):
                    xLocation = xLocation + 1
                    print("█   You walk along the beach to the East.")
                    location = locationName[6]
                    break
                elif (moveDirection.upper() == "S"):
                    yLocation = yLocation - 1
                    print("█   You swim out to the edge of the coast.")
                    location = locationName[19]
                    break
                elif (moveDirection.upper() == "W"):
                    xLocation = xLocation - 1
                    print("█   You walk along to the end of the beach.")
                    location = locationName[22]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")
            elif (xLocation == 1) and (yLocation == -1) and (zLocation == 0): #Oceanic Bridge
                print("█")
                print("█   What direction would you like to move in?")
                moveDirection = input("█   [South (S) ¦ West (W) ¦ Return (R)]: ")
                print("█")
                if (moveDirection.upper() == "S"):
                    yLocation = yLocation + 1
                    print("█   You walk along the stable bridge out over the coast.")
                    location = locationName[18]
                    break
                elif (moveDirection.upper() == "W"):
                    xLocation = xLocation - 1
                    print("█   You walk back along the sandy beach. ")
                    location = locationName[6]
                    break
                elif (moveDirection.upper() == "R"):
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    movementVar0 = 1
                else:
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid reponse.  ║")
                    print("█ ║      Please select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")

    elif (actionChoice == "2"):#Inspect
        print("█")

        if (xLocation == -1) and (yLocation == 0) and (zLocation == 0):
            if (townHallAccess == True):
                print("█   You try to open the door but it is locked.")
                print("█")

        elif (xLocation == -1) and (yLocation == -1) and (zLocation == 0):
            print("█   What shop would you like to browse in?")
            shopChoice = int(input("█   [Potion/Food Shop (1) ¦ Item Shop (2)]: "))
            while(shopChoice == 1):
                print("█")
                print("█   You enter the Potion / Food shop and see two stalls.")
                print("█   One stall has potions and one has food.")
                print("█")
                print("█   What one would you like to see?")
                stallChoice = int(input("█   [Potions Stall (1) ¦ Food Stall (2) ¦ Return (3)]: "))
                if (stallChoice == 1):
                    print("█")
                    print("█   You walk up to the potions stall.")
                    print("█   You speak to the man behind the stall")
                    print("█")
                    while (stallChoice == 1):
                        print("█              ┌───────────────────────────────────────────────┐")
                        print("█   Server ────┤\"Welcome to our shop, how may I be of service?\"│")
                        print("█              └───────────────────────────────────────────────┘")
                        potionStallChoice1 = int(input("█       [Buy (1) ¦ Sell (2) ¦ Return (3)]: "))
                        print("█")
                        if (potionStallChoice1 == 1):
                            print("█")
                            print("█      ┌────────────────────────┐")
                            print("█      │Can I see what you sell?├─── ", name, "")
                            print("█      └────────────────────────┘")
                            print("█")
                            while (potionStallChoice1 == 1):#Buy
                                print("█      ╔══════════════════════════════════════════════╗")
                                print("█      ║ Shop Stock:                                  ║")
                                sfsPSListVar1 = int(0)
                                while (sfsPSListVar1 < len(sfsPotionShopItems)):
                                    print("█      ║ ", (sfsPSListVar1 + 1), ") ", sfsPotionShopItems[sfsPSListVar1], "    ->    ", mS, sfsPotionShopPrices[sfsPSListVar1], "   ║")
                                    sfsPSListVar1 = sfsPSListVar1 + 1
                                print("█      ║  0 )    ~~~Return to Previous Menu~~~        ║")
                                print("█      ╠══════════════════════════════════════════════╣")
                                print("█      ║ What would you like to buy? [ 0 ~", len(sfsPotionShopItems), "]        ║")
                                print("█      ╠══════════════════╦═══════════════════════════╝")
                                print("█      ║ Current Balance: ║", mS, moneyPouch)
                                print("█      ╚══════════════════╝")
                                print("█")
                                purchaseItem = int(input("█      Purchase Item Number: "))
                                if (purchaseItem == 0):
                                    print("█")
                                    print("█ ┌─────────────────────────────┐")
                                    print("█ │ ~~~Previous menu opened.~~~ │")
                                    print("█ └─────────────────────────────┘")
                                    print("█")
                                    break
                                elif (purchaseItem <= len(sfsPotionShopItems)) and (purchaseItem > 0):
                                    purchaseQuant = int(input("█      Purchase Quantity: "))
                                    purchaseCost = sfsPotionShopPrices[purchaseItem - 1] * purchaseQuant
                                    if(purchaseQuant == 0):
                                        print("█")
                                        print("█      ╔════════════════════════════════╗")
                                        print("█      ║   You can not purchase 0 of:   ║")
                                        print("█      ║     ", sfsPotionShopItems[purchaseItem - 1], "      ║")
                                        print("█      ╚════════════════════════════════╝")
                                        print("█")
                                    else:
                                        if (int(purchaseCost) <= int(moneyPouch)):
                                            print("█")
                                            print("█      ╔════════════════════════════════╗")
                                            print("█      ║  You have purchased: ", purchaseQuant , "       ║")
                                            print("█      ║  of ", sfsPotionShopItems[purchaseItem - 1], "      ║")
                                            print("█      ╠════════════════════╦═══════════╝")
                                            if (sfsPotionShopItems[purchaseItem - 1] in potionPouch):
                                                potionLocation = potionPouch.index(sfsPotionShopItems[purchaseItem - 1])
                                                potionQuant[potionLocation] = potionQuant[potionLocation] + purchaseQuant
                                            else:
                                                potionPouch = list(potionPouch) + [(sfsPotionShopItems[purchaseItem - 1]),]
                                                potionQuant = potionQuant + [purchaseQuant]
                                            moneyPouch = moneyPouch - purchaseCost
                                            print("█      ║ Remaining Balance: ║", mS, moneyPouch)
                                            print("█      ╚════════════════════╝")
                                            print("█")
                                        else:
                                            print("█")
                                            print("█ ╔════════════════════════════════╗")
                                            print("█ ║  You do not have enough money  ║")
                                            print("█ ║     to purchase that much.     ║")
                                            print("█ ╚════════════════════════════════╝")
                                            print("█")
                                else:
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║  That is not a valid reponse.  ║")
                                    print("█ ║      Please select again.      ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
                        elif (potionStallChoice1 == 2):
                            print("█")
                            print("█          ┌─────────────────────┐")
                            print("█          │I am looking to sell.├─── ", name, "")
                            print("█          └─────────────────────┘")
                            print("█")
                            while (potionStallChoice1 == 2):#Sell
                                print("█      ╔═══════════════════════════════════════════════════╗")
                                print("█      ║ Potion Inventory:                                 ║")
                                sfsPSListVar2 = int(0)
                                while (sfsPSListVar2 < len(potionPouch)):
                                    print("█      ║ ", (sfsPSListVar2 + 1), ") [",potionQuant[sfsPSListVar2] ,"]", potionPouch[sfsPSListVar2], "    ->    ", mS, sfsPotionShopPrices[sfsPotionShopItems.index(potionPouch[sfsPSListVar2])], "   ║")
                                    sfsPSListVar2 = sfsPSListVar2 + 1
                                
                                print("█      ║  0 )    ~~~Return to Previous Menu~~~             ║")
                                print("█      ╠═══════════════════════════════════════════════════╣")
                                print("█      ║ What would you like to sell? [ 0 ~", len(potionPouch), "]            ║")
                                print("█      ╠══════════════════╦════════════════════════════════╝")
                                print("█      ║ Current Balance: ║", mS, moneyPouch)
                                print("█      ╚══════════════════╝")
                                print("█")
                                saleItem = int(input("█      Item Number to Sell: "))
                                if (saleItem == 0):
                                    print("█")
                                    print("█ ┌─────────────────────────────┐")
                                    print("█ │ ~~~Previous menu opened.~~~ │")
                                    print("█ └─────────────────────────────┘")
                                    print("█")
                                    break
                                elif (saleItem <= len(potionPouch)) and (saleItem > 0):
                                    saleQuant = int(input("█      Ammount to Sell: "))
                                    saleCost = sfsPotionShopPrices[sfsPotionShopItems.index(potionPouch[saleItem - 1])] * saleQuant
                                    if(saleQuant == 0):
                                        print("█")
                                        print("█      ╔════════════════════════════════╗")
                                        print("█      ║   You can not sell 0 of:       ║")
                                        print("█      ║     ", potionPouch[saleItem - 1], "      ║")
                                        print("█      ╚════════════════════════════════╝")
                                        print("█")
                                    else:
                                        if (potionQuant[saleItem - 1] >= saleQuant):
                                            print("█")
                                            print("█      ╔════════════════════════════════╗")
                                            print("█      ║  You have sold: ", saleQuant , "            ║")
                                            print("█      ║  of ", potionPouch[saleItem - 1], "      ║")
                                            print("█      ╠══════════════╦═════════════════╝")
                                            if (potionQuant[saleItem - 1] == saleQuant):
                                                del potionPouch[saleItem - 1]
                                                del potionQuant[saleItem - 1]
                                            else:
                                                potionQuant[saleItem - 1] = int(potionQuant[saleItem - 1]) - int(saleQuant)
                                            moneyPouch = moneyPouch + saleCost
                                            print("█      ║ New Balance: ║", mS, moneyPouch)
                                            print("█      ╚══════════════╝")
                                            print("█")
                                        else:
                                            print("█")
                                            print("█ ╔════════════════════════════════╗")
                                            print("█ ║     You do not have enough     ║")
                                            print("█ ║   potions to sell that much.   ║")
                                            print("█ ╚════════════════════════════════╝")
                                            print("█")
                                else:
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║  That is not a valid reponse.  ║")
                                    print("█ ║      Please select again.      ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
                        elif (potionStallChoice1 == 3):#Return
                            potionStallChoice1 = 0
                            stallChoice = 0
                        else:
                            print("█")
                            print("█ ╔════════════════════════════════╗")
                            print("█ ║  That is not a valid reponse.  ║")
                            print("█ ║      Please select again.      ║")
                            print("█ ╚════════════════════════════════╝")
                            print("█")
                            potionStallChoice1 = 0
                elif (stallChoice == 2):
                    print("█")
                    print("█   You walk up to the food stall.")
                    print("█   You speak to the man behind the stall")
                    print("█")
                    while (stallChoice == 2):
                        print("█              ┌───────────────────────────────────────────────┐")
                        print("█   Server ────┤\"Welcome to our shop, how may I be of service?\"│")
                        print("█              └───────────────────────────────────────────────┘")
                        print("█")
                        foodStallChoice1 = int(input("█   [Buy (1) ¦ Sell (2) ¦ Return (3)]: "))
                        if (foodStallChoice1 == 1):
                            print("█")
                            print("█      ┌────────────────────────┐")
                            print("█      │Can I see what you sell?├─── ", name, "")
                            print("█      └────────────────────────┘")
                            print("█")
                            while (foodStallChoice1 == 1):#Buy
                                print("█      ╔══════════════════════════════════════════════╗")
                                print("█      ║ Shop Stock:                                  ║")
                                sfsFSListVar1 = int(0)
                                while (sfsFSListVar1 < len(sfsFoodShopItems)):
                                    print("█      ║ ", (sfsFSListVar1 + 1), ") ", sfsFoodShopItems[sfsFSListVar1], "    ->    ", mS, sfsFoodShopPrices[sfsFSListVar1], "     ║")
                                    sfsFSListVar1 = sfsFSListVar1 + 1
                                print("█      ║  0 )    ~~~Return to Previous Menu~~~        ║")
                                print("█      ╠══════════════════════════════════════════════╣")
                                print("█      ║ What would you like to buy? [ 0 ~", len(sfsFoodShopItems), "]        ║")
                                print("█      ╠══════════════════╦═══════════════════════════╝")
                                print("█      ║ Current Balance: ║", mS, moneyPouch)
                                print("█      ╚══════════════════╝")
                                print("█")
                                purchaseItem = int(input("█      Purchase Item Number: "))
                                if (purchaseItem == 0):
                                    print("█")
                                    print("█ ┌─────────────────────────────┐")
                                    print("█ │ ~~~Previous menu opened.~~~ │")
                                    print("█ └─────────────────────────────┘")
                                    print("█")
                                    break
                                elif (purchaseItem <= len(sfsFoodShopItems)) and (purchaseItem > 0):
                                    purchaseQuant = int(input("█      Purchase Quantity: "))
                                    purchaseCost = sfsFoodShopPrices[purchaseItem - 1] * purchaseQuant
                                    if(purchaseQuant == 0):
                                        print("█")
                                        print("█      ╔════════════════════════════════╗")
                                        print("█      ║   You can not purchase 0 of:   ║")
                                        print("█      ║     ", sfsFoodShopItems[purchaseItem - 1], "        ║")
                                        print("█      ╚════════════════════════════════╝")
                                        print("█")
                                    else:
                                        if (int(purchaseCost) <= int(moneyPouch)):
                                            print("█")
                                            print("█      ╔════════════════════════════════╗")
                                            print("█      ║  You have purchased: ", purchaseQuant , "       ║")
                                            print("█      ║  of ", sfsFoodShopItems[purchaseItem - 1], "        ║")
                                            print("█      ╠════════════════════╦═══════════╝")
                                            if (sfsFoodShopItems[purchaseItem - 1] in foodPouch):
                                                foodLocation = foodPouch.index(sfsFoodShopItems[purchaseItem - 1])
                                                foodQuant[foodLocation] = foodQuant[foodLocation] + purchaseQuant
                                            else:
                                                foodPouch = list(foodPouch) + [(sfsFoodShopItems[purchaseItem - 1]),]
                                                foodQuant = foodQuant + [purchaseQuant]
                                            moneyPouch = moneyPouch - purchaseCost
                                            print("█      ║ Remaining Balance: ║", mS, moneyPouch)
                                            print("█      ╚════════════════════╝")
                                            print("█")
                                        else:
                                            print("█")
                                            print("█ ╔════════════════════════════════╗")
                                            print("█ ║  You do not have enough money  ║")
                                            print("█ ║     to purchase that much.     ║")
                                            print("█ ╚════════════════════════════════╝")
                                            print("█")
                                else:
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║  That is not a valid reponse.  ║")
                                    print("█ ║      Please select again.      ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
                        elif (foodStallChoice1 == 2):
                            print("█")
                            print("█          ┌─────────────────────┐")
                            print("█          │I am looking to sell.├─── ", name, "")
                            print("█          └─────────────────────┘")
                            print("█")
                            while (foodStallChoice1 == 2):#Sell
                                print("█      ╔═════════════════════════════════════════════════╗")
                                print("█      ║ Food Inventory:                                 ║")
                                sfsFSListVar2 = int(0)
                                while (sfsFSListVar2 < len(foodPouch)):
                                    print("█      ║ ", (sfsFSListVar2 + 1), ") [",foodQuant[sfsFSListVar2] ,"]", foodPouch[sfsFSListVar2], "    ->    ", mS, sfsFoodShopPrices[sfsFoodShopItems.index(foodPouch[sfsFSListVar2])], "   ║")
                                    sfsFSListVar2 = sfsFSListVar2 + 1
                                
                                print("█      ║  0 )    ~~~Return to Previous Menu~~~           ║")
                                print("█      ╠═════════════════════════════════════════════════╣")
                                print("█      ║ What would you like to sell? [ 0 ~", len(foodPouch), "]          ║")
                                print("█      ╠══════════════════╦══════════════════════════════╝")
                                print("█      ║ Current Balance: ║", mS, moneyPouch)
                                print("█      ╚══════════════════╝")
                                print("█")
                                saleItem = int(input("█      Item Number to Sell: "))
                                if (saleItem == 0):
                                    print("█")
                                    print("█ ┌─────────────────────────────┐")
                                    print("█ │ ~~~Previous menu opened.~~~ │")
                                    print("█ └─────────────────────────────┘")
                                    print("█")
                                    break
                                elif (saleItem <= len(foodPouch)) and (saleItem > 0):
                                    saleQuant = int(input("█      Ammount to Sell: "))
                                    saleCost = sfsFoodShopPrices[sfsFoodShopItems.index(foodPouch[saleItem - 1])] * saleQuant
                                    if(saleQuant == 0):
                                        print("█")
                                        print("█      ╔════════════════════════════════╗")
                                        print("█      ║   You can not sell 0 of:       ║")
                                        print("█      ║     ", foodPouch[saleItem - 1], "        ║")
                                        print("█      ╚════════════════════════════════╝")
                                        print("█")
                                    else:
                                        if (foodQuant[saleItem - 1] >= saleQuant):
                                            print("█")
                                            print("█      ╔════════════════════════════════╗")
                                            print("█      ║  You have sold: ", saleQuant , "            ║")
                                            print("█      ║  of ", foodPouch[saleItem - 1], "        ║")
                                            print("█      ╠══════════════╦═════════════════╝")
                                            if (foodQuant[saleItem - 1] == saleQuant):
                                                del foodPouch[saleItem - 1]
                                                del foodQuant[saleItem - 1]
                                            else:
                                                foodQuant[saleItem - 1] = int(foodQuant[saleItem - 1]) - int(saleQuant)
                                            moneyPouch = moneyPouch + saleCost
                                            print("█      ║ New Balance: ║", mS, moneyPouch)
                                            print("█      ╚══════════════╝")
                                            print("█")
                                        else:
                                            print("█")
                                            print("█ ╔════════════════════════════════╗")
                                            print("█ ║     You do not have enough     ║")
                                            print("█ ║     food to sell that much.    ║")
                                            print("█ ╚════════════════════════════════╝")
                                            print("█")
                                else:
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║  That is not a valid reponse.  ║")
                                    print("█ ║      Please select again.      ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
                        elif (foodStallChoice1 == 3):#Return
                            foodStallChoice1 = 0
                            stallChoice = 0
                        else:
                            print("█")
                            print("█ ╔════════════════════════════════╗")
                            print("█ ║  That is not a valid reponse.  ║")
                            print("█ ║      Please select again.      ║")
                            print("█ ╚════════════════════════════════╝")
                            print("█")
                            foodStallChoice1 = 0
                    stallChoice = 0
                    
#############################################################################################################################################################

                    
                shopChoice = 0


##
##                                            print("█")
##                                            print("█      ╔════════════════════════════════╗")
##                                            print("█      ║  You have sold: ", saleQuant , "            ║")
##                                            print("█      ║  of ", foodPouch[saleItem - 1], "        ║")
##                                            print("█      ╠══════════════╦═════════════════╝")
##                                            if (foodQuant[saleItem - 1] == saleQuant):
##                                                del foodPouch[saleItem - 1]
##                                                del foodQuant[saleItem - 1]
##                                            else:
##                                                foodQuant[saleItem - 1] = int(foodQuant[saleItem - 1]) - int(saleQuant)
##                                            moneyPouch = moneyPouch + saleCost
##                                            print("█      ║ New Balance: ║", mS, moneyPouch)
##                                            print("█      ╚══════════════╝")
##
##
##




        elif (xLocation == -1) and (yLocation == 1) and (zLocation == 0):
            tempVarLoop1 = 0
            while (tempVarLoop1 == 0):
                itemsListVar1 = int(0)
                print("█      ╔════════════════════════════════╗")
                print("█      ║  Pouch Inventory:              ║")
                while (itemsListVar1 < len(itemsList)):
                    print("█      ║  ", (itemsListVar1 + 1), ") ", itemsList[itemsListVar1], "    ->    ", itemQuant[itemsListVar1], "    ║")
                    itemsListVar1 = itemsListVar1 + 1
                print("█      ║  Pouch Quantity: ", sum(itemQuant), "/30        ║")
                print("█      ╠════════════════════════════════╣")
                print("█      ║  Bank Inventory:               ║")
                bankListVar1 = int(0)
                while (bankListVar1 < len(bankedItems)):
                    print("█      ║  ", (bankListVar1 + 1), ") ", bankedItems[bankListVar1], "    ->    ", bankedItemsQuant[bankListVar1], "    ║")
                    bankListVar1 = bankListVar1 + 1
                print("█      ║  Bank Quantity: ", sum(bankedItemsQuant), "/150       ║")
                print("█      ╚════════════════════════════════╝")
                print("█")
                choice = input("█   [Withdraw (W) ¦ Deposit (D) ¦ Close Bank (C)]: ")
                if (choice.upper() == "W"):#Withdraw
                    print("█")
                    if (len(bankedItems) == 0):
                        print("█")
                        print("█ ╔════════════════════════════════╗")
                        print("█ ║  Your bank is currently EMPTY  ║")
                        print("█ ║  You cannot withdraw from it.  ║")
                        print("█ ╚════════════════════════════════╝")
                        print("█")
                        tempVarBankWithdrawEmpty = input("█   Click Return (Enter) to coninue: ")
                    else:
                        witemID = int(input("█   Item to withdraw: "))
                        wquantity = int(input("█   Quantity to withdraw: "))
                        if ((witemID <= len(bankedItems)) and (witemID > 0)):
                            if (sum(itemQuant) + int(wquantity) > int(itemsBagCapacity)):
                                print("█")
                                print("█ ╔════════════════════════════════╗")
                                print("█ ║  You do not have enough bank   ║")
                                print("█ ║       space to do this.        ║")
                                print("█ ╚════════════════════════════════╝")
                                print("█")
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
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║    You cannot move 0 of an     ║")
                                    print("█ ║     item to your inventory.    ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
                                    time.sleep(2)
                                elif(wquantity > bankedItemsQuant[witemID - 1]):
                                    if (bankedItems[witemID - 1] in itemsList):
                                        tempVar = itemsList.index(bankedItems[witemID - 1])
                                        itemQuant[tempVar] = itemQuant[tempVar] + bankedItemsQuant[witemID - 1]
                                        bankedItemsQuant[witemID - 1] = 0
                                    else:
                                        itemsList = list(itemsList) + [(bankedItems[witemID - 1]),]
                                        itemQuant = itemQuant + wquan
                                        bankedItemsQuant[witemID - 1] = int(bankedItemsQuant[witemID - 1]) - wquantity
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║   Withdrawn maximum ammount.   ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
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
                        else:
                            print("█")
                            print("█ ╔════════════════════════════════╗")
                            print("█ ║  That is not a valid item ID.  ║")
                            print("█ ║Select a value within the range.║")
                            print("█ ║      Please select again.      ║")
                            print("█ ╚════════════════════════════════╝")
                            print("█")
                elif (choice.upper() == "D"):
                    print("█")
                    if (len(itemsList) == 0):
                        print("█")
                        print("█ ╔════════════════════════════════╗")
                        print("█ ║ Your pouch is currently empty. ║")
                        print("█ ║   You cannot deposit from it.  ║")
                        print("█ ╚════════════════════════════════╝")
                        print("█")
                        tempVarBankDepositEmpty = input("█   Click Return (Enter) to coninue: ")
                    else:#if there are items in bank
                        itemID = int(input("█   Item to deposit: "))
                        quantity = int(input("█   Quantity to deposit: "))
                        if ((itemID <= len(itemsList)) and (itemID > 0)):
                            if (sum(bankedItemsQuant) + int(quantity) > int(bankSize)):
                                print("█")
                                print("█ ╔════════════════════════════════╗")
                                print("█ ║  You do not have enough space  ║")
                                print("█ ║    in your bank to do this.    ║")
                                print("█ ╚════════════════════════════════╝")
                                print("█")
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
                                elif(quantity == 0):
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║    You cannot move 0 of an     ║")
                                    print("█ ║     item to your inventory.    ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
                                    time.sleep(2)
                                elif(quantity > itemQuant[itemID - 1]):
                                    if (itemsList[itemID - 1] in bankedItems):
                                        tempVar = bankedItems.index(itemsList[itemID - 1])
                                        bankedItemsQuant[tempVar] = bankedItemsQuant[tempVar] + itemQuant[itemID - 1]
                                        itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                                    else:
                                        bankedItems = list(bankedItems) + [(itemsList[itemID - 1]),]
                                        bankedItemsQuant = bankedItemsQuant + quan
                                        itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity

                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║   Deposited Maximum Ammount    ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
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
                                elif(quantity < itemQuant[itemID - 1]) and (quantity > 0):
                                    if (itemsList[itemID - 1] in bankedItems):
                                        tempVar = bankedItems.index(itemsList[itemID - 1])
                                        bankedItemsQuant[tempVar] = bankedItemsQuant[tempVar] + quantity
                                        itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                                    else:
                                        bankedItems = list(bankedItems) + [(itemsList[itemID - 1]),]
                                        bankedItemsQuant = bankedItemsQuant + [quantity]
                                        itemQuant[itemID - 1] = int(itemQuant[itemID - 1]) - quantity
                        else:
                            print("█")
                            print("█ ╔════════════════════════════════╗")
                            print("█ ║  That is not a valid item ID.  ║")
                            print("█ ║Select a value within the range.║")
                            print("█ ║      Please select again.      ║")
                            print("█ ╚════════════════════════════════╝")
                            print("█")
                elif (choice.upper() == "C"):#Return
                    print("█")
                    print("█ ┌─────────────────────────────┐")
                    print("█ │ ~~~Previous menu opened.~~~ │")
                    print("█ └─────────────────────────────┘")
                    print("█")
                    tempVarLoop1 = 1
                else:#Error
                    print("█")
                    print("█ ╔════════════════════════════════╗")
                    print("█ ║  That is not a valid Response  ║")
                    print("█ ║      Please Select again.      ║")
                    print("█ ╚════════════════════════════════╝")
                    print("█")


    elif (actionChoice == "3"):#Equipment
#        Equipment()




        currentWeapon = 0
        equipmentVar = 0
        while(equipmentVar == 0):
            print("█")
            print("█   Equipment Options:")
            print("█   Current Wealth: ", mS  , moneyPouch)
            equipmentChoice1 = int(input("█   [View Armour (1) ¦ View Weapons (2) ¦ View Bag (3) ¦ Eat Food (4) ¦ Return (5)]: "))
            if (equipmentChoice1 == 1): #ViewArmour
                print("█")
                print("█   Helm:   ",armourTypes[currentHelmType])
                print("█   Body:   ",armourTypes[currentBodyType])
                print("█   Legs:   ",armourTypes[currentLegsType])
                print("█   Boot:   ",armourTypes[currentBootType])
                equipmentVar2 = 0
                while(equipmentVar2 == 0):
                    print("█")
                    print("█")
                    print("█")
                    print("█   More Information:")
                    armourChoice1 = int(input("█   [Helm Stats (1) ¦ Body Stats (2) ¦ Legs Stats (3) ¦ Boot Stats (4) ¦ Return (5)]: "))
                    if(armourChoice1 == 1):
                        print("█")
                        print("█    Helm  Type: ",armourTypes[currentHelmType])
                        print("█    Helm Defence: ",helmDefence[currentHelmType])
                    elif (armourChoice1 == 2):
                        print("█")
                        print("█    Body Type: ",armourTypes[currentBodyType])
                        print("█    Body Defence: ",helmDefence[currentBodyType])
                    elif (armourChoice1 == 3):
                        print("█")
                        print("█    Legs Type: ",armourTypes[currentLegsType])
                        print("█    Legs Defence: ",legsDefence[currentLegsType])
                    elif (armourChoice1 == 4):
                        print("█")
                        print("█    Boot Type: ",armourTypes[currentBootType])
                        print("█    Boot Defence: ",bootDefence[currentBootType])
                    elif (armourChoice1 == 5):
                        print("█")
                        print("█ ┌─────────────────────────────┐")
                        print("█ │ ~~~Previous menu opened.~~~ │")
                        print("█ └─────────────────────────────┘")
                        print("█")
                        equipmentVar2 = 1
                    else:
                        print("█")
                        print("█ ╔════════════════════════════════╗")
                        print("█ ║  That is not a valid Response  ║")
                        print("█ ║      Please Select again.      ║")
                        print("█ ╚════════════════════════════════╝")
                        print("█")
            elif (equipmentChoice1 == 2):#ViewWeapons
                while (equipmentChoice1 == 2):
                    print("█")
                    print("█")
                    print("█   Current Weapon:    ", weapons[currentWeapon])
                    print("█")
                    print("█   Weapon Options:")
                    weaponChoice1 = int(input("█   [List Weapons (1) ¦ Get Weapon Stats (2) ¦ Return (3)]: "))
                    if (weaponChoice1 == 1):#ListWeapons
                        print("█")
                        print("█   Owned Weapons:")
                        weaponslist = int(0)
                        while (weaponslist < len(weapons)):
                            print("█   ",(weaponslist + 1), "): ", weapons[weaponslist], "    ", activeWeapon[weaponslist])
                            weaponslist = weaponslist + 1
                        print("█")
                        weaponChoiceVar2 = 0
                        while(weaponChoiceVar2 == 0):
                            print("█   Weapon Choices: ")
                            weaponChoice2 = int(input("█   [Swap Weapons (1)¦ Return (2)]: "))
                            if (weaponChoice2 == 1):#SwapWeapons
                                print("█")#Fill in
                                print("█   What weapon would you like to swap with? [ 1 ~", len(weapons) , "]:")
                                swapChoice = int(input("█   Swap Number: "))
                                if (swapChoice < len(weapons) + 1) and (swapChoice > 0): #If valid answer
                                    activeWeapon[currentWeapon] = ""
                                    currentWeapon = swapChoice - 1
                                    activeWeapon[currentWeapon] = "*Equipped*"
                                    print("█")
                                    print("█   These are the statistics for your now equipped weapon.")
                                    print("█    Weapon: ", weapons[currentWeapon])
                                    print("█    Type:   ", weaponTypes[currentWeapon])
                                    print("█    Damage: ", weaponDamages[currentWeapon])
                                else:#Error
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║  That is not a valid Response  ║")
                                    print("█ ║      Please Select again.      ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")
                                weaponChoiceVar2 = 1
                            elif (weaponChoice2 == 2):#Return
                                print("█")
                                print("█ ┌─────────────────────────────┐")
                                print("█ │ ~~~Previous menu opened.~~~ │")
                                print("█ └─────────────────────────────┘")
                                print("█")
                                weaponChoiceVar2 = 1
                                equipmentChoice1 = 0
                            else:#Error
                                print("█")
                                print("█ ╔════════════════════════════════╗")
                                print("█ ║  That is not a valid Response  ║")
                                print("█ ║      Please Select again.      ║")
                                print("█ ╚════════════════════════════════╝")
                                print("█")
                                weaponChoiceVar2 = 1

                        equipmentChoice1 = 0
                    elif (weaponChoice1 == 2):#GetWeaponStats
                        print("█")
                        print("█   These are the statistics for your current weapon.")
                        print("█    Weapon: ", weapons[currentWeapon])
                        print("█    Type:   ", weaponTypes[currentWeapon])
                        print("█    Damage: ", weaponDamages[currentWeapon])
                        equipmentChoice1 = 0
                    elif (weaponChoice1 == 3):#Return
                        print("█")
                        print("█ ┌─────────────────────────────┐")
                        print("█ │ ~~~Previous menu opened.~~~ │")
                        print("█ └─────────────────────────────┘")
                        print("█")
                        equipmentChoice1 = 0
                    else:#Error
                        print("█")
                        print("█ ╔════════════════════════════════╗")
                        print("█ ║  That is not a valid Response  ║")
                        print("█ ║      Please Select again.      ║")
                        print("█ ╚════════════════════════════════╝")
                        print("█")
            elif (equipmentChoice1 == 3):#ViewBag
                print("█")
                bagVar1 = 0
                while(bagVar1 == 0):
                    print("█   What pouch would you like to view: ")
                    bagChoice = int(input("█   [Items (1) ¦ Quest Items (2) ¦ Return (3)]: "))
                    if(bagChoice == 1):#Items
                        print("█")
                        print("█   Pouch Items:")
                        itemsListVar1 = int(0)
                        while (itemsListVar1 < len(itemsList)):
                            print("█ ",(itemsListVar1 + 1), ") ", itemsList[itemsListVar1], "    ->    ", itemQuant[itemsListVar1])
                            itemsListVar1 = itemsListVar1 + 1
                        print("█")
                        print("█   Pouch Quantity: ", sum(itemQuant), " /50")   #INC Custom Bag Pouches
                        itemChoiceVar = 0
                        while(itemChoiceVar == 0):
                            print("█   What would you like to do: ")
                            itemChoiceVar2 = int(input("█   [Drop Item (1) ¦ Use Item (2) ¦ Inspect (3) ¦ Return (4)]: "))
                            print("█")
                            if(itemChoiceVar2 == 1):#DropItem
                                print("█   What item would you like to drop? [ 0 ~", len(itemsList), "]:")
                                itemDropID = int(input("█   Item ID to Drop: "))
                                if(itemDropID < len(weapons) + 1) and (itemDropID > 0): #If valid answer)
                                    itemDropQuantVar = 0
                                    while(itemDropQuantVar == 0):
                                        print("█")
                                        print("█   How many of", itemsList[itemDropID - 1], "would you like to drop? [0 ~", itemQuant[itemDropID - 1], "]:")
                                        if (len(itemsList) == 0):
                                            print("█")
                                            print("█   You do not have any items to drop.")
                                        else:
                                            itemDropQuant = int(input("█   Number of items to drop: "))
                                            if(itemDropQuant <= itemQuant[itemDropID - 1]) and (itemDropQuant >= 0):
                                                if (itemDropQuant == 0):
                                                    print("█")
                                                    print("█   You have dropped nothing.")
                                                    itemDropQuantVar = 1
                                                else:
                                                    itemQuant[itemDropID - 1] = itemQuant[itemDropID - 1] - itemDropQuant
                                                    itemDropQuantVar = 1
                                                    print("█")
                                                    print("█   You have dropped", itemDropQuant, "of", itemsList[itemDropID - 1])
                                                    print("█   You have", itemQuant[itemDropID - 1], "remaining.")
                                                    print("█")
                                            else: #Error
                                                print("█")
                                                print("█ ╔════════════════════════════════╗")
                                                print("█ ║  That is not a valid Response  ║")
                                                print("█ ║      Please Select again.      ║")
                                                print("█ ╚════════════════════════════════╝")
                                                print("█")
                                        if(itemQuant[itemDropID - 1] == 0):
                                            temp1 = list(itemsList)
                                            temp2 = list(itemQuant)
                                            z = 0
                                            itemsList = []
                                            itemQuant = []
                                            while(z < itemDropID - 1):
                                                itemsList = itemsList + [temp1[z]]
                                                itemQuant = itemQuant + [temp2[z]]
                                                z = z + 1
                                            z = itemDropID
                                            while(z < len(temp1)):
                                                itemsList = itemsList + [temp1[z]]
                                                itemQuant = itemQuant + [temp2[z]]
                                                z = z + 1
                                            z = 0
                                else:#Error
                                    print("█")
                                    print("█ ╔════════════════════════════════╗")
                                    print("█ ║  That is not a valid Response  ║")
                                    print("█ ║      Please Select again.      ║")
                                    print("█ ╚════════════════════════════════╝")
                                    print("█")

                            elif(itemChoiceVar2 == 2):#UseItem
                                ...
                            elif(itemChoiceVar2 == 3):#Inspect
                                ...
                            elif(itemChoiceVar2 == 4):#Return
                                print("█")
                                print("█ ┌─────────────────────────────┐")
                                print("█ │ ~~~Previous menu opened.~~~ │")
                                print("█ └─────────────────────────────┘")
                                print("█")
                                itemChoiceVar = 1
                            else:#Error
                                print("█")
                                print("█ ╔════════════════════════════════╗")
                                print("█ ║  That is not a valid Response  ║")
                                print("█ ║      Please Select again.      ║")
                                print("█ ╚════════════════════════════════╝")
                                print("█")
                        print("█")
                    elif(bagChoice == 2):#QuestItems
                        print("█")
                    elif(bagChoice == 3):#Return
                        print("█")
                        print("█ ┌─────────────────────────────┐")
                        print("█ │ ~~~Previous menu opened.~~~ │")
                        print("█ └─────────────────────────────┘")
                        print("█")
                        bagVar1 = 1
                    else:#Error
                        print("█")
                        print("█ ╔════════════════════════════════╗")
                        print("█ ║  That is not a valid Response  ║")
                        print("█ ║      Please Select again.      ║")
                        print("█ ╚════════════════════════════════╝")
                        print("█")
            elif (equipmentChoice1 == 4):#Eat Food
                print("█")
                print("█ ┌─────────────────────────────┐")
                print("█ │ ~~~Previous menu opened.~~~ │")
                print("█ └─────────────────────────────┘")
                print("█")
                equipmentVar = 1
            elif (equipmentChoice1 == 5):#Return
                print("█")
                print("█ ┌─────────────────────────────┐")
                print("█ │ ~~~Previous menu opened.~~~ │")
                print("█ └─────────────────────────────┘")
                print("█")
                equipmentVar = 1
            else:#Error
                print("█")
                print("█ ╔════════════════════════════════╗")
                print("█ ║  That is not a valid Response  ║")
                print("█ ║      Please Select again.      ║")
                print("█ ╚════════════════════════════════╝")
                print("█")








    elif (actionChoice == "4"):#ExitGame
        print("█")
        saveGame = input("█   Would you like to save the game? [Y/N]: ")
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
        print("█")
        print("█ ╔════════════════════════════════╗")
        print("█ ║    ~~~~Now Exiting Game~~~~    ║")
        print("█ ╚════════════════════════════════╝")
        print("█")
        alive = False
    else:#Error
        print("█")
        print("█ ╔════════════════════════════════╗")
        print("█ ║  That is not a valid Response  ║")
        print("█ ║      Please Select again.      ║")
        print("█ ╚════════════════════════════════╝")
        print("█")


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
##    ##    ##  each memory fragment gives a new skill
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
