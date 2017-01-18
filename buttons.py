import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)

del sys.argv[0]

#def CheckInputs(pins):
for pin_str in sys.argv:#pins:
    pin = int(pin_str)
    GPIO.setup(pin, GPIO.IN)
    if(GPIO.input(pin)==1):
        print(pin)#return pin
#    return 0
