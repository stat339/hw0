import matplotlib.pyplot as plt
import numpy as np


x = np.array([-10, 10])

plt.plot(x, x, "r--", x, 2*x, "b--", x, 3*x, 'g--' )

plt.show()