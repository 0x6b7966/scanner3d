import numpy as np
import matplotlib.pyplot as plt

img = np.fromfile("./depth_frontal_mate20.depth", dtype=np.uint16).reshape(640, 480) & 0x1FFF
plt.imshow(img, vmin=3000, vmax=4500)
plt.show()

