import time
import buttons

print("Mode 1")
print("Input at port " + str(buttons.WaitForInput([24])))
print()

time.sleep(1)

print("Mode 2")
while(True):
    button = buttons.CheckInputs([23,24,25])
    if(button!=0):
        print("Button " + str(button) + " pressed")
        break
