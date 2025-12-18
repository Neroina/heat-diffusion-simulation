import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

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

for x, y, val in sources:
    T[x, y] = val

# ------------------ FIGURA ------------------
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

im = ax.imshow(T, cmap="inferno", vmin=0, vmax=100)
cbar = plt.colorbar(im, ax=ax)
ax.set_title("Difuzie termică 2D")

# ------------------ SLIDER ------------------
ax_alpha = plt.axes([0.2, 0.15, 0.6, 0.03])
alpha_slider = Slider(
    ax=ax_alpha,
    label="Coeficient difuzie (alpha)",
    valmin=0.01,
    valmax=0.25,
    valinit=0.15,
    valstep=0.01
)

# ------------------ STARE SIMULARE (fără global) ------------------
state = {"running": True}

# ------------------ BUTON PLAY / PAUSE ------------------
ax_button = plt.axes([0.82, 0.05, 0.12, 0.05])
play_button = Button(ax_button, "❚❚")

def toggle(event):
    state["running"] = not state["running"]
    play_button.label.set_text("▶" if not state["running"] else "❚❚")

play_button.on_clicked(toggle)

# ------------------ UPDATE ------------------
def update(frame):
    global T

    if not state["running"]:
        return [im]

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

    for x, y, val in sources:
        T_new[x, y] = val

    T = T_new

    im.set_data(T)
    ax.set_title(f"Difuzie termică 2D – alpha = {alpha:.2f}")


    return [im]
# -----------------RESET--------------------
def reset_simulation(event):
    T[:] = 0
    for x, y, val in sources:
        T[x, y] = val
    im.set_data(T)


ax_reset = plt.axes([0.65, 0.05, 0.12, 0.05])
reset_button = Button(ax_reset, "Reset")
reset_button.on_clicked(reset_simulation)

# ------------------ ANIMAȚIE ------------------
anim = FuncAnimation(
    fig,
    update,
    frames=steps,
    interval=80,
    blit=False
)

plt.show()
