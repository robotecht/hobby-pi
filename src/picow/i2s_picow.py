import machine
import time
import rp2

# DOUT pin from microphone
DOUT_PIN = 0

# PIO program to read bits from DOUT
@rp2.asm_pio(
    in_shiftdir=rp2.PIO.SHIFT_LEFT,
    autopull=False,
    pull_thresh=32
)
def i2s_reader():
    wrap_target()
    in_(pins, 1)
    wrap()

# Set up state machine
sm = rp2.StateMachine(0, i2s_reader, freq=48000, in_base=machine.Pin(DOUT_PIN))

# Start state machine
sm.active(1)

# Read and print a few amplitude values
print("Reading amplitudes:")
for _ in range(20):
    if sm.rx_fifo():
        sample = sm.get() & 0xFFFF
        print("Amplitude:", sample)
    time.sleep(0.1)

# Stop state machine
sm.active(0)
