import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Temperature points
temperatures = [27, 28, 29, 30, 31, 32, 33, 34]

# CIE L*a*b* values for black
L = [26.036, 28.703, 34.639, 39.549, 41.175, 42.492, 43.975, 45.647]
a = [0.771, 0.556, -0.224, -0.979, -1.117, -1.135, -1.130, -1.255]
b = [16.308, 16.388, 17.015, 17.912, 17.891, 17.468, 17.005, 16.854]

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(a, b, L, c='black', label='Crna - stupnjevi °C')

# Draw a line connecting the points
ax.plot(a, b, L, color='gray', linestyle='-', linewidth=1)

# Add temperature labels
for i in range(len(temperatures)):
    ax.text(a[i], b[i], L[i], f"{temperatures[i]}°", size=8)

# Labels and legend
ax.set_xlabel('a* (Zelena <-> Crvena)')
ax.set_ylabel('b* (Plava <-> Žuta)')
ax.set_zlabel('L* (Svijetlina)')
ax.set_title('CIE L*a*b* dijagram za crnu boju')
ax.legend()

plt.tight_layout()
plt.show()
