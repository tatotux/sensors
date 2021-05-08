import RPi.GPIO as GPIO
import sys

if sys.argv[1]:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers 
    RELAIS_1_GPIO = int(sys.argv[1])
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on

