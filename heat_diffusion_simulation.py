import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.widgets import Slider, Button

# ==================================================
# CONFIGURARE SIMULARE
# ==================================================
grid_size = 50
steps = 600

# matricea temperaturilor
T = np.zeros((grid_size, grid_size))

# centru + surse de căldură
c = grid_size // 2
sources = [
    (c, c, 100),
    (c - 5, c, 80),
    (c + 5, c, 80),
    (c, c - 5, 80),
    (c, c + 5, 80),
]

# aplic sursele inițiale
for x, y, val in sources:
    T[x, y] = val

# ==================================================
# STARE SIMULARE
# ==================================================
state = {
    "running": True,
    "cmap_index": 0
}

colormaps = ["inferno", "plasma", "viridis", "coolwarm"]

# ==================================================
# FIGURĂ + IMAGINE
# ==================================================
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

im = ax.imshow(
    T,
    cmap=colormaps[state["cmap_index"]],
    vmin=0,
    vmax=100
)
cbar = plt.colorbar(im, ax=ax)
ax.set_title("Difuzie termică 2D")

# ==================================================
# SLIDER ALPHA
# ==================================================
ax_alpha = plt.axes([0.2, 0.22, 0.6, 0.03])
alpha_slider = Slider(
    ax=ax_alpha,
    label="Coeficient de difuzie (alpha)",
    valmin=0.01,
    valmax=0.25,
    valinit=0.15,
    valstep=0.01
)

# ==================================================
# BUTON PLAY / PAUSE
# ==================================================
ax_play = plt.axes([0.78, 0.08, 0.14, 0.06])
play_button = Button(ax_play, "❚❚")

def toggle_play(event):
    state["running"] = not state["running"]
    play_button.label.set_text("▶" if not state["running"] else "❚❚")

play_button.on_clicked(toggle_play)

# ==================================================
# BUTON RESET
# ==================================================
ax_reset = plt.axes([0.42, 0.08, 0.14, 0.06])
reset_button = Button(ax_reset,"Reset")

def reset_simulation(event):
    T[:] = 0
    for x, y, val in sources:
        T[x, y] = val
    im.set_data(T)
    fig.canvas.draw_idle()

reset_button.on_clicked(reset_simulation)

# ==================================================
# BUTON SCHIMBARE COLORMAP
# ==================================================
ax_cmap = plt.axes([0.05, 0.08, 0.28, 0.06])
cmap_button = Button(ax_cmap, "Change colormap")

def change_colormap(event):
    was_running = state["running"]
    state["running"] = False

    state["cmap_index"] += 1
    if state["cmap_index"] == len(colormaps):
        state["cmap_index"] = 0

    im.set_cmap(colormaps[state["cmap_index"]])
    fig.canvas.draw_idle()

    state["running"] = was_running

cmap_button.on_clicked(change_colormap)

# ==================================================
# FUNCȚIA DE UPDATE (ANIMATIE)
# ==================================================
def update(frame):
    if not state["running"]:
        return [im]

    alpha = alpha_slider.val
    T_new = T.copy()

    # difuzie termică (ecuația căldurii discretizată)
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

    T[:] = T_new[:]

    im.set_data(T)
    ax.set_title(f"Difuzie termică 2D | alpha = {alpha:.2f}")

    return [im]

# ==================================================
# ANIMAȚIE
# ==================================================
anim = FuncAnimation(
    fig,
    update,
    frames=steps,
    interval=80,
    blit=False
)

# ==================================================
# EXPORT GIF
# ==================================================
save_gif = False  # schimbă în True ca să generezi GIF-ul

if save_gif:
    writer = PillowWriter(fps=20)
    anim.save("heat_diffusion.gif", writer=writer)

plt.show()
