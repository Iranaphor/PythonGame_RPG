"""
----------
Items to include:
----------
Drift Tomes: used to teleport the player to a specific coordinate from a list
teleportDictionary("LocationName":(x, y, z))
----------

"""
import time
import random
import os


x = int(0)
y = int(0)
z = int(0)



l01ap10 = "[][][][][][][][][][][][][][][[][][]["
l01ap09 = "                                    "
l01ap08 = "                                    "
l01ap07 = "                                    "
l01ap06 = "   This is the farvest backdrop     "
l01ap05 = "                                    "
l01ap04 = "                                    "
l01ap03 = "                                    "
l01ap02 = "                                    "
l01ap01 = "                                    "
l01ac00 = "                                    "
l01an01 = "                                    "
l01an02 = "                                    "
l01an03 = "                                    "
l01an04 = "                                    "
l01an05 = "                                    "
l01an06 = "                                    "
l01an07 = "                                    "
l01an08 = "                                    "
l01an09 = "                                    "
l01an10 = "                                    "

l02ap10 = "                                    "
l02ap09 = "                                    "
l02ap08 = "                                    "
l02ap07 = "                                    "
l02ap06 = "                                    "
l02ap05 = "                                    "
l02ap04 = "------------------------------------"
l02ap03 = "------------------------------------"
l02ap02 = "------------------------------------"
l02ap01 = "   This is the next backdrop        "
l02ac00 = "------------------------------------"
l02an01 = "------------------------------------"
l02an02 = "------------------------------------"
l02an03 = "                                    "
l02an04 = "                                    "
l02an05 = "                                    "
l02an06 = "                                    "
l02an07 = "                                    "
l02an08 = "                                    "
l02an09 = "                                    "

l03ap10 = "                                    "
l03ap09 = "                                    "
l03ap08 = "                                    "
l03ap07 = "                                    "
l03ap06 = "                                    "
l03ap05 = "                                    "
l03ap04 = "                                    "
l03ap03 = "                                    "
l03ap02 = "                                    "
l03ap01 = "                                    "
l03ac00 = "                                    "
l03an01 = "                                    "
l03an02 = "                                    "
l03an03 = "===================================="
l03an04 = "===================================="
l03an05 = "===================================="
l03an06 = "=============Third=================="
l03an07 = "===================================="
l03an08 = "===================================="
l03an09 = "===================================="
l03an10 = "===================================="


def menuMain(location):
    absolutely_unused_variable = os.system("cls")
    print("╔══════════════════════════════════════════════════╦══════════════════════════╗")
    print("╠══════════════════════════════════════════════════╣", ''.join(map(str, l04)), "║")
    print("║                                                  ║", ''.join(map(str, l05)), "║")
    print("║                                                  ║", ''.join(map(str, l06)), "║")
    print("║                                                  ║", ''.join(map(str, l07)), "║")
    print("║                                                  ║", ''.join(map(str, l08)), "║")
    print("║                                                  ║", ''.join(map(str, l09)), "║")
    print("║                                                  ║", ''.join(map(str, l10)), "║")
    print("║                                                  ║", ''.join(map(str, l11)), "║")
    print("║                                                  ║", ''.join(map(str, l12)), "║")
    print("║                                                  ║", ''.join(map(str, l13)), "║")
    print("║                                                  ║", ''.join(map(str, l14)), "║")
    print("║                                                  ║", ''.join(map(str, l15)), "║")
    print("║                                                  ╠══════════════════════════╣")
    print("║                                                  ║What would you like to do?║")
    print("║                                                  ╠──────────────┬───────────╣")
    print("║                                                  ║ Move         │ (N/E/S/W) ║")
    print("║                                                  ║ Inspect      │ (I)       ║")
    print("║                                                  ║ Backpack     │ (B)       ║")
    print("║                                                  ║ Save / Quit  │ (Q)       ║")
    print("╠══════════════════════════════════════════════════╩══════════════╩═══════════╝")



l01 = (l01ap10, l01ap09, l01ap08, l01ap07, l01ap06, l01ap05, l01ap04, l01ap03, l01ap02, l01ap01, l01ac00, l01an01, l01an02, l01an03, l01an04, l01an05, l01an06, l01an07, l01an08, l01an09, l01an10)
l02 = (l02ap10, l02ap09, l02ap08, l02ap07, l02ap06, l02ap05, l02ap04, l02ap03, l02ap02, l02ap01, l02ac00, l02an01, l02an02, l02an03, l02an04, l02an05, l02an06, l02an07, l02an08, l02an09, l02an10)lines [lo1, lo2, lo3]
l03 = (l03ap10, l03ap09, l03ap08, l03ap07, l03ap06, l03ap05, l03ap04, l03ap03, l03ap02, l03ap01, l03ac00, l03an01, l03an02, l03an03, l03an04, l03an05, l03an06, l03an07, l03an08, l03an09, l03an10)
lines = (l01, l02, l03)

a = True
lo = 13

while (a):
    lineList = lines[z]

    while (z > 0):
        
    
    menuMain((lineList[y])[x - 2])

    
    nav = input("╚═Direction: ")


    if (nav.upper() == "Q"):
        exit()








