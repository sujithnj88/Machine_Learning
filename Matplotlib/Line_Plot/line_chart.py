import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 30, 1000)
y = np.sin(x) + 0.5 * x

plt.plot(x, y)
plt.savefig("line_chart.png")
