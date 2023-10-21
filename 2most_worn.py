#!/usr/bin/python3
from collections import Counter
from colors_data import colors_data

all_colors = [color for colors in colors_data.values() for color in colors]

most_common_color = Counter(all_colors).most_common(1)[0][0]
print("Most worn color throughout the week:", most_common_color)
