import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np

def generate_palette(base_color, num_colors):
    base_rgb = np.array(mcolors.hex2color(base_color))
    black_rgb = np.array([0, 0, 0])
    palette = [(1 - i / (num_colors - 1)) * base_rgb + (i / (num_colors - 1)) * black_rgb for i in range(num_colors)]
    return [mcolors.to_hex(color) for color in palette]

base_color = "#D8F6FF"
num_colors = 40

palette = generate_palette(base_color, num_colors)

palette_rgb = [mcolors.hex2color(color) for color in palette]

fig, ax = plt.subplots(figsize=(10, 2), subplot_kw=dict(xticks=[], yticks=[], frame_on=False))
ax.imshow([palette_rgb], aspect='auto')


for idx, color in enumerate(palette):
    print(f'{idx + 1}. {color}')
plt.show()
