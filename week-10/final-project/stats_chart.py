import os
import subprocess
import sys
from datetime import datetime

import matplotlib.pyplot as plt

CHART_STATS = ["hp", "attack", "defense", "speed"]
CHARTS_DIR = "charts"


def build_chart_data(pokemon_list):
    chart_data = {stat: [] for stat in CHART_STATS}
    for pokemon in pokemon_list:
        for stat in CHART_STATS:
            chart_data[stat].append(pokemon["stats"].get(stat, 0))
    return chart_data


def save_stats_chart(pokemon_list, output_dir=CHARTS_DIR):
    names = [pokemon["name"].title() for pokemon in pokemon_list]
    chart_data = build_chart_data(pokemon_list)

    os.makedirs(output_dir, exist_ok=True)

    bar_width = 0.2
    positions = range(len(names))
    fig, ax = plt.subplots(figsize=(8, 5))

    for i, stat in enumerate(CHART_STATS):
        offsets = [pos + i * bar_width for pos in positions]
        ax.bar(offsets, chart_data[stat], width=bar_width, label=stat.title())

    ax.set_xlabel("Pokemon")
    ax.set_ylabel("Base Stat Value")
    ax.set_title("Which Pokemon has the strongest base stats?")
    ax.set_xticks([pos + bar_width * 1.5 for pos in positions])
    ax.set_xticklabels(names)
    ax.legend(title="Stat")
    fig.tight_layout()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = "stats_comparison_" + timestamp + ".png"
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath)
    plt.close(fig)

    open_chart(filepath)

    return filepath


def open_chart(filepath):
    if sys.platform == "darwin":
        subprocess.run(["open", filepath], check=False)
    elif sys.platform == "win32":
        os.startfile(filepath)
    else:
        subprocess.run(["xdg-open", filepath], check=False)
