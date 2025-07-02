from machine import Pin
import time

led = Pin("LED",Pin.OUT) #Set up pin 16 connected with LED

while True:
    led.value(1) #LED ON
    time.sleep(2) #Sleep
    
    led.value(0) #LED OFF
    time.sleep(2) #Sleep 2s