import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# ------------------ CONFIGURARE ------------------
grid_size = 50
steps = 500

T = np.zeros((grid_size, grid_size))

c = grid_size // 2
sources = [
    (c, c, 100),
    (c-5, c, 80),
    (c+5, c, 80),
    (c, c-5, 80),
    (c, c+5, 80),
]

# aplic sursele inițial
for x, y, val in sources:
    T[x, y] = val

# ------------------ FIGURA ------------------
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

im = ax.imshow(T, cmap="inferno", vmin=0, vmax=100)
cbar = plt.colorbar(im, ax=ax)
ax.set_title("Difuzie termică 2D")

# ------------------ SLIDER ALPHA ------------------
ax_alpha = plt.axes([0.2, 0.1, 0.6, 0.03])
alpha_slider = Slider(
    ax=ax_alpha,
    label="Coeficient difuzie (alpha)",
    valmin=0.01,
    valmax=0.25,
    valinit=0.15,
    valstep=0.01
)

# ------------------ UPDATE ------------------
def update(frame):
    global T

    alpha = alpha_slider.val
    T_new = T.copy()

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

    # surse constante
    for x, y, val in sources:
        T_new[x, y] = val

    T = T_new

    im.set_data(T)
    ax.set_title(f"Difuzie termică 2D – Pasul {frame} | alpha = {alpha:.2f}")

    return [im]

# ------------------ ANIMAȚIE ------------------
anim = FuncAnimation(
    fig,
    update,
    frames=steps,
    interval=80,
    blit=False
)

plt.show()
