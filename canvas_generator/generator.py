import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def hexa_to_rgb_percent(cs):
    r, g, b = cs[1:3], cs[3:5], cs[5:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r / 256, g / 256, b / 256)

tiles = pd.read_csv("tile_placements.csv")
tiles.sort_values("ts", inplace=True)
colors = ['#FFFFFF', '#E4E4E4', '#888888', '#222222', '#FFA7D1', '#E50000', '#E59500', '#A06A42', 
          '#E5D900', '#94E044', '#02BE01', '#00E5F0', '#0083C7', '#0000EA', '#E04AFF', '#820080']

colors_percent = [hexa_to_rgb_percent(color) for color in colors]

image = np.zeros((1001, 1001, 3))

for index, row in tiles.iterrows():
    image[row["y_coordinate"], row["x_coordinate"]] = colors_percent[row["color"]]
    print(index)
fig = plt.figure(figsize=(24, 24))
plt.imsave("canva.png", image)