import matplotlib.pyplot as plt
import numpy as np

y = [
    -0.151,
    -0.107,
    -0.088,
    -2.334,
    9.995,
    -1.401,
    -0.137,
    0.181,
    0.723,
    1.533,
    1.86,
    1.24,
    0.415,
    -0.02,
    -0.063,
    -0.273,
    0.249,
    0.195,
    -0.156,
    -0.054,
    0.088,
    0.166,
    0.132,
    0.215,
    0.093,
]

x = np.linspace(0, 1.2, 25)

plt.plot(x, y)
plt.xlabel("Time in seconds", fontsize=22)
plt.ylabel("Voltage in V", fontsize=22)
plt.show()
