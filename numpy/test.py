import numpy as np

a = np.arange(12).reshape((4,3))
print(a)

print(a[:,2])

print(a[a[:,2] < 7])