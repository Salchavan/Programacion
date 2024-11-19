import os
import time
so = 1
sec = 0
min = 0
hr = 0
day = 0
cl = lambda: os.system("cls")
while so != 0:
    sec = sec + 1
    if sec == 60:
        min = min + 1
        sec = 0
    if min == 60:
        hr = hr + 1
        min = 0
    if hr == 24:
        day = day + 1
        hr = 0
    print(f"{day}:{hr}:{min}:{sec}")
    time.sleep(1)
    cl()
