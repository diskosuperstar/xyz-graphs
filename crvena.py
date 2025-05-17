import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Temperature points
temperatures = [43, 44, 45, 47, 48, 49, 50]

L = [58.798, 65.799, 70.298, 77.113, 79.868, 82.032, 82.805]
a = [57.366, 47.542, 40.068, 27.315, 21.803, 17.380, 15.700]
b = [33.578, 21.535, 15.422, 7.995, 5.753, 4.232, 3.936]


# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(a, b, L, c='red', label='Crvena - stupnjevi °C')

# Draw a line connecting the points
ax.plot(a, b, L, color='black', linestyle='-', linewidth=1)

# Add temperature labels
for i in range(len(temperatures)):
    ax.text(a[i], b[i], L[i], f"{temperatures[i]}°", size=8)

# Labels and legend
ax.set_xlabel('a* (Zelena <-> Crvena)')
ax.set_ylabel('b* (Plava <-> Žuta)')
ax.set_zlabel('L* (Svijetlina)')
ax.set_title('CIE L*a*b* dijagram za crvenu boju')
ax.legend()

plt.tight_layout()
plt.show()
