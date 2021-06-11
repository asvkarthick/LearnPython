# Author : Karthick Kumaran <asvkarthick@gmail.com>
# Program to plot realtime/offline gyro/accelerometer 3-axis data

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

def animate(i):
    x = []
    y = []
    z = []
    with open('gyro.txt') as f:
        lines = f.readlines();
        for line in lines:
            line = line.split(' ')
            line = [i.strip() for i in line]
            x.append(int(line[2]) / 100)
            y.append(int(line[3]) / 100)
            z.append(int(line[4]) / 100)

    plt.cla()
    plt.plot(x, color='r', label='x')
    plt.plot(y, color='g', label='y')
    plt.plot(z, color='b', label='z')

ani = FuncAnimation(plt.gcf(), animate, 1000)
plt.tight_layout()
plt.show()
