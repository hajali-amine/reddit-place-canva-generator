from cgitb import reset
from typing import Tuple
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Generator:
    def __init__(self) -> None:
        self.tiles = pd.read_csv("tile_placements.csv")
        self.tiles.sort_values("ts", inplace=True, ignore_index=True)


    def hexa_to_rgb_percent(self, cs: str) -> Tuple:
        r, g, b = cs[1:3], cs[3:5], cs[5:]
        r, g, b = [int(n, 16) for n in (r, g, b)]
        return (r / 256, g / 256, b / 256)

    def generate_picture_from_time(self, time):
        # colors https://lospec.com/palette-list/r-place
        colors = ['#FFFFFF', '#E4E4E4', '#888888', '#222222', '#FFA7D1', '#E50000', '#E59500', '#A06A42', 
                '#E5D900', '#94E044', '#02BE01', '#00E5F0', '#0083C7', '#0000EA', '#E04AFF', '#820080']

        colors_percent = [self.hexa_to_rgb_percent(color) for color in colors]

        image = np.full((1001, 1001, 3), 255 / 255)

        for index, row in self.tiles.iterrows():
            image[row["y_coordinate"], row["x_coordinate"]] = colors_percent[row["color"]]
            print(index)
            if row["ts"] == time:
                break
        
        plt.figure(figsize=(24, 24))
        plt.imsave(f"canvas/{time}.png", image)