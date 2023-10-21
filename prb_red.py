#!/usr/bin/python3
from collections import Counter
from colors_data import colors_data

all_colors = [color for colors in colors_data.values() for color in colors]

probability_red = all_colors.count('RED') / len(all_colors)
print("Probability of getting red:", probability_red)
