# %%
import matplotlib.pyplot as plt

import numpy as np


x = np.linspace(0, 5, 11)
y = x ** 2
print('x = ', x)
print('y = ', y, '\n')

fig, axes = plt.subplots(nrows=1, ncols=2)

for current_ax in axes:
    current_ax.plot(x, y)

fig, axes = plt.subplots(nrows=1, ncols=2)

plt.tight_layout()
axes[0].plot(x, y)
axes[0].set_title('First Plot')

axes[1].plot(y, x)
axes[1].set_title('Second Plot')

fig = plt.figure(figsize=(3, 2))

ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)

fig, axes = plt.subplots(figsize=(3, 2))

axes.plot(x, y)

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(3, 2))

plt.tight_layout()
axes[0].plot(x, y)
axes[1].plot(y, x)

fig.savefig('graph.png', dpi=200)

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, label='X Squared')
ax.plot(x, x ** 3, label='X Cubed')

ax.legend(loc=10)

ax.set_title('Title')
ax.set_ylabel('y_label')
ax.set_xlabel('x_label')


fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y, label='X Squared')
ax.plot(x, x ** 3, label='X Cubed')

ax.legend(loc=(0.1, 0.1))

# %%
