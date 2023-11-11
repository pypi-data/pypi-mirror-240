import matplotlib.pyplot as plt
import numpy as np
import torch


a = torch.zeros((3, 32, 32))

for i in range(20, 24):
    for j in range(20, 24):
        a[0][i][j] = 255

a = a.numpy()
a = np.transpose(a, (1, 2, 0))
plt.imshow(a)
plt.show()
