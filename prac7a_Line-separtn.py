import numpy as np
import matplotlib.pyplot as plt

def create_distance_function(a, b, c):
    """Creates a distance function for the line 0 = ax + by + c."""
    def distance(x, y):
        norm = a * x + b * y + c
        if norm == 0:
            pos = 0
        elif (norm < 0 and b < 0) or (norm > 0 and b > 0):
            pos = -1
        else:
            pos = 1
        return (np.abs(norm) / np.sqrt(a**2 + b**2), pos)
    return distance

# Define points and plot
points = [(3.5, 1.8), (1.1, 3.9)]
fig, ax = plt.subplots()
ax.set_xlabel("sweetness")
ax.set_ylabel("sourness")
ax.set_xlim([-1, 6])
ax.set_ylim([-1, 8])
size=10
# Plot points
for index, (x, y) in enumerate(points):
    if index == 0:
        ax.plot(x, y, "o", color="darkorange", markersize=size, label="Point 1")
    else:
        ax.plot(x, y, "o", color="blue", markersize=size, label="Point 2")
        step=0.05

# Generate and plot lines
X = np.arange(-0.5, 5, 0.1)
#step = 0.05

for x in np.arange(0, 1 + step, step):
    slope = np.tan(np.arccos(x))
    dist4line1 = create_distance_function(slope, -1, 0)

    Y = slope * X
    results = []
    
    for point in points:
        results.append(dist4line1(*point))

    if results[0][1] != results[1][1]:
        ax.plot(X, Y, "g-", label="Dividing Line" if x == 0 else "")
    else:
        ax.plot(X, Y, "r-", label="Non-dividing Line" if x == 0 else "")

ax.legend()
plt.show()
