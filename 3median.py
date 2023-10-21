#!/ust/bin/pythpn3
from collections import Counter
from colors_data import colors_data

def calculate_median_color(colors):
    sorted_colors = sorted(colors)
    n = len(sorted_colors)
    if n % 2 == 1:
        return sorted_colors[n // 2]
    else:
        return (sorted_colors[n // 2 - 1], sorted_colors[n // 2])

all_colors = [color for colors in colors_data.values() for color in colors]

median_color = calculate_median_color(all_colors)
print("Median color:", median_color)
