from machine import ADC, Pin
import time

force_sensor = ADC(Pin(28))

while True:
    reading = force_sensor.read_u16() // 64  # Scale to 0–1023
    print(reading)
    time.sleep(0.1)
