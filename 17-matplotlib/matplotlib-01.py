# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Program to plot single axis gyro realtime/offline data

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# plt.style.use('fivethirtyeight')

def animate(i):
    x = []
    y = []
    with open('gyro.txt') as f:
        lines = f.readlines();
        for line in lines:
            line = line.split(' ')
            line = [i.strip() for i in line]
            x.append(line[0])
            y.append(int(line[2]) / 100)

    plt.cla()
    plt.plot(y)

ani = FuncAnimation(plt.gcf(), animate, 1000)
plt.tight_layout()
plt.show()
