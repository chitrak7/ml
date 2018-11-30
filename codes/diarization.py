
import matplotlib.pyplot as plt
import numpy as np

for i in [(4,4), (-4,-4)]:
    a = np.random.uniform(0,2,100)
    b = np.random.uniform(0,2*np.pi,100)
    c = [i[0] +a[j]*(np.sin(b[j])) for j in range(100)]
    d = [i[1] +a[j]*(np.cos(b[j])) for j in range(100)]
    plt.scatter(c,d, c="b")

for i in [(-4,4), (4,-4)]:
    a = np.random.uniform(0,2,100)
    b = np.random.uniform(0,2*np.pi,100)
    c = [i[0] +a[j]*(np.sin(b[j])) for j in range(100)]
    d = [i[1] +a[j]*(np.cos(b[j])) for j in range(100)]
    plt.scatter(c,d, c="r")

plt.show()
