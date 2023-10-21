#!/usr/bin/python3
from collections import Counter
from colors_data import colors_data

all_colors = [color for colors in colors_data.values() for color in colors]

def calculate_variance(colors):
    mean = sum(colors) / len(colors)
    variance = sum((x - mean) ** 2 for x in colors) / len(colors)
    return variance

color_frequencies = Counter(all_colors).values()
variance = calculate_variance(color_frequencies)

print("Variance of color frequencies:", variance)
