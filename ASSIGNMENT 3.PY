ASSIGNMENT 3

NAME : S.DHANALAKSHMI 
ROLL NO : 732319106003

Python code for blinking of LED light:

CODE :

import RPi.GPIO as GPIO
import time
LED_PIN = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
while true:
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(1) GPIO.output(LED_PIN,
GPIO.LOW)
time.sleep(1)
GPIO.cleanup()

Python code for traffic lights :

CODE :

from gpiozero import LED from
time import sleep
lights = TrafficLights(27, 5, 8)
while True:

light.green.on()
sleep(1)
lights.amber.on()
sleep(1)
lights.red.on()
sleep(1) lights.off()