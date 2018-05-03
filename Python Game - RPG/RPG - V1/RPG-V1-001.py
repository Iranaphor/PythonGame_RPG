import time
import datetime
i = 10
while ( i < 11 ):
    print ("i:", i)
    i = i - 1
    time.sleep(0.5)
#    print (datetime.datetime.now().time())
    if (i < 1):
        i = 10
