from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import time

f = lambda x: (x**2 - 40)
fp = lambda x: (2*x)

x = np.linspace(-10,10)
y1 = np.array([f(i) for i in x])

fig, ax = plt.subplots()
ax.set(xlim=(-10,10), ylim=(-50,50))
ax.plot(x, y1)
plt.axhline(0, color="black")
plt.axvline(0, color="black")

xn = 2.5

lbl = None
for _ in range(20):
    print(xn)
    tangent = lambda x: fp(xn) * (x-xn) + f(xn)
    y2 = np.array([tangent(i) for i in x])
    ax.plot(x, y2)
    if lbl:
        lbl.set_visible(False)
    lbl = plt.text(xn, 0, str(xn)) 
    # y - f(xn) = fp(xn) * (x-xn)
    xn = xn - f(xn)/fp(xn)
    plt.ginput()

plt.show()
