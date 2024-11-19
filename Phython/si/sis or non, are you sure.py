import random
import time
n = 3

while(n != 0):
    n -= 1
    decision = random.randint(0, 1)
    print(decision)
    sure = random.randint(0, 1)
    print(sure)
    if decision == 1:
        print("Yes or No: YES")
        time.sleep(0.5)
        if sure == 1:
            print("Are you sure?: YES")
            time.sleep(0.5)
            break;
        else: 
            print("Are you sure: NO")
            time.sleep(0.5)
    else:
        print("Yes or No: NO")
        if sure == 1:
            print("Are you sure: YES")
            time.sleep(0.5)
            break;
        else: 
            print("Are you sure: NO")
            time.sleep(0.5)
    time.sleep(1)
    print("----------------------------")
