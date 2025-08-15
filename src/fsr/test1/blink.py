# MicroPython script for Raspberry Pi Pico to read values from a force-sensitive resistor (FSR)
# This code is free to use and modify for any purpose

from machine import ADC, Pin
import time

# Set up the analog pin connected to the force sensor (FSR)
FSR_PIN = 28  # GP28 corresponds to ADC2 on the Pico
fsr = ADC(Pin(FSR_PIN))

# Function to interpret force level based on analog reading
def interpret_force(value):
    if value < 102:
        return "no pressure"
    elif value < 205:
        return "light touch"
    elif value < 512:
        return "light squeeze"
    elif value < 819:
        return "medium squeeze"
    else:
        return "big squeeze"

# Main loop to continuously read and display force sensor data
while True:
    raw_value = fsr.read_u16()           # Read 16-bit analog value (0–65535)
    scaled_value = raw_value // 64       # Convert to 10-bit scale (0–1023)

    print("Force sensor reading =", scaled_value)
    print(" ->", interpret_force(scaled_value))

    time.sleep(1)  # Wait for 1 second before next reading
