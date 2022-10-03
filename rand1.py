import numpy as np
rows = 3
cols = 3
a = np.matrix(np.random.randint(1,10, size=(rows, cols)))
b = np.matrix(np.random.randint(10,20, size=(rows, cols)))
print(a)
print(b)
c = a*b
print(c)


