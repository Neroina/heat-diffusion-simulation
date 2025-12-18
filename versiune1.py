import numpy as np
import matplotlib.pyplot as plt

grid_size = 50
steps = 200

# matricea temperaturilor
T = np.zeros((grid_size, grid_size))

# sursa de căldură în centru
center = grid_size // 2
T[center, center] = 100

# simularea difuziei
for step in range(steps):
    T_new = T.copy()  # creez o copie separata a matricei T

    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            T_new[i, j] = (
                T[i - 1, j] +   # sus
                T[i + 1, j] +   # jos
                T[i, j - 1] +   # stânga
                T[i, j + 1]     # dreapta
            ) / 4

    T = T_new  # actualizez matricea (trec la urmatorul moment de timp)

# afișare
plt.imshow(T, cmap="inferno")
plt.colorbar(label="Temperatura")
plt.title("Difuzie termică 2D – varianta 1")
plt.show()
