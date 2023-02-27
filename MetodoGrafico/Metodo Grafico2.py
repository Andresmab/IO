import matplotlib.pyplot as plt
import numpy as np
import math
plt.style.use('seaborn')


x=np.linspace(0,50,1000)
y=np.linspace(0,50,1000)

def f(x):
    return -3/2 * x + 60
def g(x):
    return -x/2 + 40

def f(y):
    return 40 - 2/3*y

def g(y):
    return 80 - 2*y

fig, ax =plt.subplots()
ax.plot(x,f(x))
ax.plot(x,g(x))
ax.plot(y,f(y))
ax.plot(y,g(y))


xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()
ax.grid(True, linestyle='-')


ax.annotate("", xy=(xmax, 0), xytext=(xmin,0),
            arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))

ax.annotate("", xy=(0, ymax), xytext=(0,ymin),
            arrowprops=dict(color='gray', width=1.5, headwidth=8, headlength=10))

plt.show()