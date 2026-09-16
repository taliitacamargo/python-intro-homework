# PokeDex CLI

A command-line tool for looking up Pokemon, built with Python and the [PokeAPI](https://pokeapi.co/).

## API used

[PokeAPI](https://pokeapi.co/) (`https://pokeapi.co/api/v2/pokemon/{name}`) — no API key required.

## Install and run

From this folder (`week-10/final-project/`):

```bash
pip install -r requirements.txt
python main.py
```

## CLI interaction

When you run the program, it asks you to type a Pokemon name. It then looks that Pokemon up and prints its height, weight, types, and base stats. Type `quit` to exit.

If you type a name that isn't a real Pokemon, or leave the input blank, the program prints a friendly message and asks you to try again instead of crashing.

Type `compare` to build a chart instead of looking up a single Pokemon. You'll be asked for two or more Pokemon names (comma-separated); the program fetches each one and saves a bar chart comparing their base stats.

## Extension track

**Option A: Visualization**

## Visualization

The `compare` command answers the question: **which Pokemon has the strongest base stats among the ones I look up?**

It fetches base HP, Attack, Defense, and Speed for each Pokemon entered and plots them as a grouped bar chart, saved as a PNG under `charts/` (filenames include a timestamp via Python's `datetime` module so repeated runs don't overwrite each other). A sample chart comparing Pikachu, Charizard, and Snorlax is included at `charts/stats_comparison_20260915-230306.png`.

I chose a grouped bar chart because the goal is to compare several discrete, unrelated categories (individual Pokemon) across several stats at once. Bars make it easy to read exact heights and compare across both Pokemon and stat type, which a line chart (implying a trend over a continuum) wouldn't communicate as clearly.

**Main takeaway from the sample chart:** Snorlax has by far the highest HP and Attack of the three, but the tradeoff is clear — its Speed is the lowest, while Charizard is fastest and Pikachu is weakest in raw stats overall despite decent Speed.

## Video demo

https://www.loom.com/share/0421626ddc5b4e898ab9728d75296cde
