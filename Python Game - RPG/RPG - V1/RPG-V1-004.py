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

def weapon():
    print ("What weapon would you like to use?")
    print ("Fist ¦ Sword ¦ Mace")
    weaponChoice = input()
    if (weaponChoice == "Fist"):
        weaponDamage = fistAttack
    if (weaponChoice == "Sword"):
        weaponDamage = swordAttack
    if (weaponChoice == "Mace"):
        weaponDamage = maceAttack
    print ("")

def ownDam():
    ownDamage = (baseDamage + weaponDamage + attackLevel + (int(random.random() * 10 ) - 5))


def resetBat():
    creatureDamage = 1
    creatureHealth = 100

#####################
print ("You encounter a hostile bat.")
print ("It flies past you.")
print ("The bat comes back towards you, leftclick to begin attacking it!")
resetBat()
decision = input()
if(decision == "leftclick"):
    maxHealth = defenceLevel + 20
    ownHealth = maxHealth
    weapon()
while (decision == "leftclick"):
    ownDam()
    while (creatureHealth > 0):
        attackChance = int(random.random() * 10)
        print()
        print ("You swing your weapon!")
        time.sleep(1)
        if (attackChance > 3):
            creatureHealth = (creatureHealth - ownDam())
            print ("You damaged the creature by, ", int(ownDam()))
            attackExp = attackExp + batAttackExp
            if (creatureHealth < 0):
                creatureHealth = 0
            print ("The CREATURE'S health is now at: ", creatureHealth)
            if (int(attackExp) == 0):
                attackLevel = attackLevel + 1
                ownDam()
                print ("")
                print ("Congratulations!")
                print ("Your Attack Level has been raised!")
                print ("Your Attack Level is now at:", attackLevel)
                print ("You now deal additional Damage during a fight.")
                print("")
        else:
            print ("You missed!")
            print ("The creature did damage to you.")
            ownHealth = ownHealth - creatureDamage
            print ("YOUR health is now at: ", ownHealth)
            defenceExp = defenceExp + batDefenceExp
            if (int(defenceExp) == 0):
                defenceLevel = defenceLevel + 1
                maxHealth = defenceLevel + 20
                ownHealth = maxHealth
                print ("")
                print ("Congratulations!")
                print ("Your Defence Level has been raised!")
                print ("Your Defence Level is now at:", defenceLevel)
                print ("Your health has been increased to, ",maxHealth)
                print ("And your health has been restored to it's max.")
                print("")
        decsion = ""
        while (creatureHealth == 0):
            print ("")
            print ("You have slain the creature!")
            print ("Another bat comes out of the darkness, would you like to attack it?")
            print ("Leftclick to continue the fighting!")
            decision = input()
            resetBat()
    break
