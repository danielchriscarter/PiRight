import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)

del sys.argv[0]

for pin_str in sys.argv:
    pin = int(pin_str)
    GPIO.setup(pin, GPIO.IN)
    if(GPIO.input(pin)==1):
        print(pin)
GPIO.cleanup()
