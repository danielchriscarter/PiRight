import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

def CheckInputs(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.IN)
        if(GPIO.input(pin)==1):
            return pin
    return 0

def WaitForInput(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.IN)
    while(True):
        for pin in pins:
            if(GPIO.input(pin)==1):
                return pin
        time.sleep(0.1)

