import time

t = 0
pause = False

while pause == False:
    time.sleep(1)
    t += 1
    print (t)
    if t == 10:
        pause = True


