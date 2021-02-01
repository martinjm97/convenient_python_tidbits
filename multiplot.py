import matplotlib.pyplot as plt


def perfect_dimensions(n):
    width, i = 1, 2
    while i * i <= n:
        if n % i == 0:
            width = i
        i += 1
    return width, n // width


width, height = perfect_dimensions(len(variable_names))
fig, axs = plt.subplots(width, height)
fig.suptitle(f'My title', fontsize=26)
for k, name in enumerate(variable_names):
    i, j = k // width, k % height
    if width == 1:
        axs[j].plot(xs, ys, color='blue')
        axs[j].set(xlabel='xs', ylabel='ys', title=name)
    else:
        axs[i, j].plot(xs, ys, color='blue')
        axs[i, j].set(xlabel='xs', ylabel='ys', title=name)

plt.show()
