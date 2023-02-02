import matplotlib.pyplot as plt
import numpy as np

y = [-0.005, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.005, 0, 0, -0.005, 0, 0, -0.005, 0, -0.005, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.005, 0, -0.005, 0, 0, 0, 0, 0, 0.005, 0, 0, 0, 0, 0, 0.005, -0.005, 0, 0, 0, 0, 0, 0, 0, 0.005, 0.01, 0.015, 0.039, -0.015, -0.049, -0.029, 0, 0, 0, 0, 0, 0, 0, 0, 1.89, 7.827, -1.572, 0.205, 0.762, 0.986, 0, -1.855, -1.421, -0.889, -0.752, 0, 0.396, 0.376, 0.225, 0.654, 1.265, 0.903, 0.264, 0.137, 0.078, 0.078, 0.122, 0.181, 0.098, 0.029, 0.068, 0.049, 0.049, -0.015, 0, 0, -0.024, -0.029, -0.054, -0.02, 0.02, -0.015, -0.015, 0.01, 0, -0.034, 0.513, 0.977, 0.132, 0.161, 0.996, -0.908, -2.368, -1.729, -2.695, -1.182, 2.061, 7.466, -4.263, -4.053, -1.709, -0.645, -0.288, -0.166, -0.112, -0.083, 1.353, 9.995, -1.562, 0.459, 0.781, 1.646, 0.908, 0.068, -0.156, -0.596, -0.19, 0.234, 0.205, 0.122, -0.029, 0.049, 0.098, 0.044, 0.078, 0.073, 0.244, 0.356, 0.396, 0.186, -0.815, -0.068, -1.523, -0.64, -0.444, -1.484, -0.806, -0.264, 1.416, 5.024, -5.068, -2.891, -1.152, -0.459, -0.225, -0.142, -0.103, -0.078, -0.063, -0.054, 2.412, 6.948, -1.406, 0.947, 0.713, 0.537, 0.352, -0.01, 0.112, -0.103, -0.195, -0.439, -0.396, -0.049, -0.718, -0.239, -0.078, 0.171, 0.405, 0.801, 0.625, -0.039, -0.298, -0.161, -0.537, -1.021, -0.576, -0.264, -0.732, -0.352, 2.104, 0.679, -4.551, -2.402, -0.928, -0.371, -0.19, -0.122, -0.088, -0.068, -0.059, -0.044, 2.227, 8.169, -1.294, 0.781, 0.532, 1.455, 1.67, -0.024, -0.601, -0.225, -0.532, -0.371, -0.186, 0.093, -0.039, -0.073, 0.112, 0.137, 0.244, 0.2, 0.513, 0.742, 0.757, 0, -0.957, -0.249, -1.299, -0.156, -0.356, -0.386, -1.094, -0.376, 0.293, 7.075, -4.194, -3.604, -1.611, -0.63, -0.288, -0.166, -0.117, -0.083, -0.068, -0.059, -1.636, 9.39, -1.064, 0.337, 1.016, 1.431, 0.864, 0.708, 0.435, 0.029, -0.293, 0.146, 0.044, 0.039, 0.283, 0.044, -0.127, -0.166, 0.161, 0.034, 0.078, 0.146, 0.322, 0.522, -0.322, -0.85, -0.718, -1.182, -1.118, -1.016, -1.733, -0.181, 1.284, 7.207, -6.191, -3.936, -1.846, -0.776, -0.361, -0.205, -0.142, -0.103, -0.083, 4.897, 7.974, -0.898, 0.464, 0.181, 1.055, 0.718, 0.371, -0.244, -0.2, -0.82, -0.386, -0.532, -0.02, 0.83, 0.571, -0.044, -0.039, 0.254, 0.518, 0.449, 0.454, 0.4, 0.342, 0.562, 0.957, -0.908, -1.23, -0.693, -0.903, -0.884, -2.119, -0.708, 0.508, 4.775, -1.182, -4.697, -2.363, -0.996, -0.43, -0.225, -0.146, -0.103, -0.078, -0.063, 5.156, 2.676, -0.156, 0.571, 1.006, 1.846, 1.982, 0.522, -0.454, -0.454, -0.464, -0.503, -0.352, -0.151, -0.142, -0.186, -0.078, 0.083, 0.063, 0.083, 0.112, 0.122, 0.137, 0.161, 0.84, -1.196, -1.387, -0.112, -0.728, -1.875, -2.28, 0.283, 1.157, 7.158, -5.22, -4.258, -2.041, -0.884, -0.4, -0.225, -0.151, -0.107, -0.088, -2.334, 9.995, -1.401, -0.137, 0.181, 0.723, 1.533, 1.86, 1.24, 0.415, -0.02, -0.063, -0.273, 0.249, 0.195, -0.156, -0.054, 0.088, 0.166, 0.132, 0.215, 0.093, 0.112, 0.112, 0.127, 0.698, -0.547, -0.43, -0.718, -0.742, -1.265, -2.095, -2.07, -1.45, -0.063, 3.54, -2.598, -5.161, -2.749, -1.211, -0.542, -0.283, -0.181, -0.127, -0.103, -0.078, 6.201, 0.586, -0.352, 0.015, 0.381, 0.991, 1.343, 1.489, 1.133, 0.337, -0.156, -0.171, -0.078, 0.215, 0.259, 0.005, -0.034, 0.044, 0.049, 0.02, -0.024, 0.005, 0.054, 0.229, 0.337, -0.972, -0.605, -0.566, -0.454, -0.913, -1.719, -2.48, -1.133, 0.283, 4.844, -4.932, -4.673, -2.393, -1.045, -0.479, -0.259, -0.171, -0.122, -0.098, -1.826, 9.995, -2.822, 0.591, 0.19, 0.62, 1.143, 1.396, 0.869, -0.034, 0.122, -0.088, 0.01, 0.068, -0.103, -0.146, -0.122, -0.122, -0.054, 0.063, 0.249, 0.293, 0.273, 0.171, 0.156, 0.137, -0.176, -1.724, -1.372, -1.494, -0.874, -0.874, -1.167, -1.904, 0.103, 1.646, 7.949, -5.869, -3.477, -1.655, -0.718, -0.352, -0.205, -0.142, -0.107, -0.083, 7.617, 5.952, -0.361, 0.547, 1.016, 1.387, 0.61, -0.806, -0.649, -0.298, -0.366, -0.327, -0.347, -0.381, -0.171, 0.01, 0.103, -0.049, 0.239, -0.073, -0.264, 0.195, 0.249, 0.42, 0.508, 3.081, -1.455, -1.572, -0.283, 0.024, -0.195, -0.522, -1.509, -1.851, -1.841, 0.752, 3.12, 5.43, -4.6, -2.813, -1.279, -0.542, -0.264, -0.161, -0.112, -0.088, 1.396, -1.318, 2.017, 0.679, 0.674, 1.538, 1.831, 1.035, -0.156, -0.327, -0.371, -0.547, -0.381, -0.19, -0.127, -0.068, 0.068, 0.049, -0.015, -0.132, -0.024, 0.029, -0.015, -0.01, 0, 0.029, 0.024, 0.078, 0.376, 0.283, -0.82, -1.074, -0.986, -0.386, -1.211, 0.679, 1.172, 8.604, -4.98, -4.077, -1.934, -0.82, -0.371, -0.21, -0.142, -0.103, -0.078, -3.379, 7.075, 1.938, 0.166, 0.557, 0.918, 1.313, 0.845, -0.049, -0.342, 0.098, 0.132, -0.181, -0.327, -0.552, -0.42, 0.063, -0.151, -0.366, -0.195, -0.078, -0.063, -0.088, -0.195, -0.259, -0.303, -0.278, -0.176, -0.073, 0, 0.039, 0.024, 0.068, 0.298, 1.182, 1.27, -1.499, -2.114, -0.981, -0.391, -0.186, -0.112, -0.078, -0.063, -0.049, -0.039, -0.034, -0.034, -0.034, -0.029, -0.029, -0.029, -0.024, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.015, -0.015, -0.015, -0.015, -0.015, -0.015, -0.015, -0.015, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.01, -0.005, -0.01, -0.005, -0.01, -0.01, -0.01, -0.005, -0.01, -0.01, -0.005, -0.01, -0.01, -0.01]

x = np.linspace(0, 41.05, 822)

plt.plot(x, y)
plt.xlabel("Time in seconds",fontsize=22)
plt.ylabel("Voltage in V",fontsize=22)
plt.show()