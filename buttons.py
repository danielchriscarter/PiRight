import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def Setup(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.IN)

def CheckPins(pins):
    for pin in pins:
        if(GPIO.input(pin)==1):
            return pin
    return 0

def Cleanup():
    GPIO.cleanup()
