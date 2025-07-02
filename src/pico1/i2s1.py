from machine import Pin, I2S
from utime import sleep
import rp2.

# I2S pin configuration
DOUT_PIN = 0  # Data from mic
BCLK_PIN = 1  # Bit clock
LRCL_PIN = 2  # Word select

# LED for visual feedback
led = Pin("LED", Pin.OUT)

# PIO program to read I2S data (simplified)
@rp2.asm_pio(in_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=False, pull_thresh=32)
def i2s_reader():
    wrap_target()
    in_(pins, 1)
    wrap()

# Set up state machine
sm = rp2.StateMachine(0, i2s_reader, freq=1000000, in_base=Pin(DOUT_PIN))
sm.active(1)

print("Reading I2S data...")

try:
    while True:
        if sm.rx_fifo():
            sample = sm.get() & 0xFFFF
            print("Amplitude:", sample)
            led.toggle()
            sleep(0.1)
except KeyboardInterrupt:
    sm.active(0)
    led.off()
    print("Stopped.")
