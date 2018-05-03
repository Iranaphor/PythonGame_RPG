import time
import datetime
import random

i = int(random.random() * 100)

while ( i < 100000):
    i = int(random.random() * 100)
    time.sleep(0.05)
    if (i == 100):
        print ("WOHOO")
    if (i == 0):
        print ("AWW")
    if (i == 50):
        print ("Meh")
    else:
        print ("i:", i)
