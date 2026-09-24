# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "pillow"]
# ///

"""Create a GIF that adds one carbon-flower petal for each year.

    uv run animate.py

Writes out/hong-kong-carbon-flower.gif.
"""

import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.colors import LinearSegmentedColormap, Normalize

from plot import DATA, OUT, rows, scale

PICTURE = "hong-kong-carbon-flower.gif"
FPS = 8


table = rows(DATA)
years = [int(row["Report_Year"]) for row in table]
totals = [float(row["Total_GHG_emissions"]) for row in table]
per_person = [float(row["Per_captia_emissions"]) for row in table]
intensity = [float(row["Carbon_Intensity"]) for row in table]

total_size = scale(totals)
person_size = scale(per_person)
number_of_years = len(years)
sector = 2 * math.pi / number_of_years
angles = [i * sector for i in range(number_of_years)]

colours = LinearSegmentedColormap.from_list(
    "carbon", ["#1f8a83", "#74b6a6", "#e6b85c", "#e06a3f"]
)
colour_scale = Normalize(vmin=min(intensity), vmax=max(intensity))

fig, ax = plt.subplots(
    figsize=(6, 6),
    subplot_kw={"projection": "polar"},
    facecolor="#0b171a",
)


def frame(index):
    """Draw the flower through the selected year."""
    ax.clear()
    ax.set_facecolor("#0b171a")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 1.14)
    ax.set_axis_off()

    for petal in range(index):
        height = 0.30 + 0.35 * total_size[petal]
        width = sector * (0.45 + 0.48 * person_size[petal])
        colour = colours(colour_scale(intensity[petal]))
        ax.bar(
            angles[petal],
            height,
            width=width,
            bottom=0.36,
            align="edge",
            color=colour,
            edgecolor="#0b171a",
            linewidth=1,
        )

    ax.text(
        0.5,
        0.53,
        "CARBON\nFLOWER",
        transform=ax.transAxes,
        color="#eaf1ec",
        fontsize=16,
        weight="bold",
        ha="center",
        va="center",
        linespacing=0.9,
    )
    ax.text(
        0.5,
        0.43,
        f"HONG KONG\n1990\u2014{years[index - 1]}\n\n{index} of {number_of_years} years",
        transform=ax.transAxes,
        color="#9fb0ad",
        fontsize=7,
        ha="center",
        va="center",
        linespacing=1.4,
    )
    return ax.patches + ax.texts


OUT.mkdir(exist_ok=True)
output = OUT / PICTURE
animation = FuncAnimation(
    fig,
    frame,
    frames=range(1, number_of_years + 1),
    interval=1000 / FPS,
    repeat_delay=1200,
)
animation.save(output, writer=PillowWriter(fps=FPS))
plt.close(fig)

print(f"saved {output}: {number_of_years} frames, {output.stat().st_size // 1024} KB")