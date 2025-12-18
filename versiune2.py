import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ------------------ CONFIGURARE ------------------
grid_size = 50
steps = 200

T = np.zeros((grid_size, grid_size))

c = grid_size // 2
T[c, c] = 100
T[c-5, c] = 80
T[c+5, c] = 80
T[c, c-5] = 80
T[c, c+5] = 80

# ------------------ FIGURA ------------------
fig, ax = plt.subplots()

im = ax.imshow(T, cmap="inferno", vmin=0, vmax=100)
cbar = plt.colorbar(im, ax=ax)
ax.set_title("Difuzie termică 2D")

# ------------------ UPDATE ------------------
def update(frame):
    global T

    T_new = T.copy()
    alpha = 0.15

    for i in range(1, grid_size - 1):
        for j in range(1, grid_size - 1):
            laplacian = (
                T[i - 1, j] +
                T[i + 1, j] +
                T[i, j - 1] +
                T[i, j + 1] -
                4 * T[i, j]
            )
            T_new[i, j] = T[i, j] + alpha * laplacian

    # SURSE ACTIVE
    T_new[c, c] = 100
    T_new[c-5, c] = 80
    T_new[c+5, c] = 80
    T_new[c, c-5] = 80
    T_new[c, c+5] = 80

    T = T_new

    im.set_data(T)
    ax.set_title(f"Difuzie termică 2D – Pasul {frame}")

    return [im]

# -------------------- ANIMAȚIE ------------------
anim = FuncAnimation(
    fig,
    update,
    frames=steps,
    interval=80,
    blit=False
)

plt.show()