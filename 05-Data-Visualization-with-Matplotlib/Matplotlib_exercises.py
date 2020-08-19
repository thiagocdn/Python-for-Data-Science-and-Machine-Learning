# %%

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 100)
y = x*2
z = x**2


fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)

fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1, ])
ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
plt.tight_layout()
ax1.plot(x, y, color='red')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.plot(x, y, color='red')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1, ])
ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.4])
plt.tight_layout()
ax1.plot(x, z)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.plot(x, y)
ax2.set_xlim([20, 22])
ax2.set_ylim([30, 50])
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))
plt.tight_layout()
axes[0].plot(x, y, lw=5, ls='--')

axes[1].plot(x, z, color='red', lw=5)

# %%
