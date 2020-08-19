# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

# lw = linewidth
# ls = linestyle
# alpha = transparency
# ax.plot(x, y, color='#FF8C00', lw=2, ls='--', marker='o', markersize=10,
#        markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='green')
ax.plot(x, y, color='purple', lw=2, ls='--')
ax.set_xlim([0, 1])
ax.set_ylim([0, 2])

# %%
