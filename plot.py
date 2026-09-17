# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

"""
Read the file in data/, make one picture, save it to out/.

    uv run plot.py

Three parts, and you will replace all three: rows() reads the file the way *your*
file needs reading, the loop in main() picks the numbers out of it, and the plot at
the bottom is the transformation you chose. Print before you plot.
"""

import json
import math
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize

FILE = "greenhouse-gas-emissions-and-carbon-intensity.json"   # CHANGE ME: the same name as in fetch.py
PICTURE = "hong-kong-carbon-flower.png"                           # what goes into out/, and into the README

HERE = Path(__file__).parent
DATA = HERE / "data" / FILE
OUT = HERE / "out"


def rows(path):
    text = path.read_text(encoding="utf-8-sig")

    if text.count("{") == text.count("}") + 1:
        text = text.rstrip()[:-1] + "}\n]"

    return json.loads(text)

def scale(values):
    """Change a list of values to numbers between 0 and 1."""
    low = min(values)
    high = max(values)
    return [(value - low) / (high - low) for value in values]
    
def main():
    table = rows(DATA)
    print(f"{DATA.name}: {len(table)} rows. The first one: {table[0]}")

    years, totals, per_person, intensity = [], [], [], []

for row in table:
    years.append(int(row["Report_Year"]))
    totals.append(float(row["Total_GHG_emissions"]))
    per_person.append(float(row["Per_captia_emissions"]))
    intensity.append(float(row["Carbon_Intensity"]))
    print(f"{DATA.name}: {len(table)} rows. The first one: {table[0]}")
print(f"one value: {totals[0]} ({type(totals[0]).__name__})")# the loop over the numbers
 def scale(values):
    low = min(values)
    high = max(values)
    return [(value - low) / (high - low) for value in values]       

total_size = scale(totals)
    person_size = scale(per_person)
    number_of_years = len(years)
    sector = 2 * math.pi / number_of_years
    angles = [i * sector for i in range(number_of_years)]

    colours = LinearSegmentedColormap.from_list(
        "carbon", ["#1f8a83", "#74b6a6", "#e6b85c", "#e06a3f"]
    )# it arrived as text; make it a number
    print(f"{len(values)} values, from {min(values)} to {max(values)}")

    fig, ax = plt.subplots( figsize=(10, 10),subplot_kw={"projection": "polar"},
    facecolor="#0b171a",)
   ax.set_facecolor("#0b171a")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
tips = []
    centres = []
    for i in range(number_of_years):  

height = 0.30 + 0.35 * total_size[i]
        width = sector * (0.45 + 0.48 * person_size[i])
        colour = colours(colour_scale(intensity[i]))

        ax.bar(
            angles[i],
            height,
            width=width,
            bottom=0.36,
            align="edge",
            color=colour,
            edgecolor="#0b171a",
            linewidth=1,
        )
        centres.append(angles[i] + width / 2)
        tips.append(0.36 + height)

    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / PICTURE, dpi=180)
    print(f"saved out/{PICTURE}")
    plt.show()


if __name__ == "__main__":
    main()
