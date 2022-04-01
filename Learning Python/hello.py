import numpy as np

x = np.array([12, 43, 2, 100, 54, 5, 68])
print(np.argsort(x))
print(np.argsort(x)[-2:][::-1])