import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Replace with your actual COM port (e.g., 'COM4' or '/dev/ttyUSB0')
ser = serial.Serial('COM4', 115200, timeout=1)

data = deque([0]*100, maxlen=100)
fig, ax = plt.subplots()
line, = ax.plot(data)
ax.set_ylim(0, 1023)
ax.set_title("Live Force Sensor Data")
ax.set_xlabel("Time")
ax.set_ylabel("Sensor Reading")

def update(frame):
    try:
        line_data = ser.readline().decode('utf-8').strip()
        if line_data.isdigit():
            data.append(int(line_data))
            line.set_ydata(data)
            line.set_xdata(range(len(data)))
    except Exception as e:
        print("Error:", e)
    return line,

ani = animation.FuncAnimation(fig, update, interval=100)
plt.show()
