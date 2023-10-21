from statistics import mode
from colors_data import colors_data

all_colors = [color for colors in colors_data.values() for color in colors]

mean_color = mode(all_colors)
print("Mean color:", mean_color)
