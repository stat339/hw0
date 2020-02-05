import numpy as np
import matplotlib.pyplot as plt


circle = plt.Circle( (0, 0) , radius=1, color="r")

fig, ax = plt.subplots()
plt.ylim(-1.25, 1.25)
plt.xlim(-1.25, 1.25)
plt.grid(linestyle='')
ax.set_aspect(1)


ax.add_artist(circle)


plt.show()