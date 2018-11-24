import numpy as np
from scipy.stats import multivariate_normal

def em_normal(data, n_class):
    mu    = []
    std   = []

    n_features = data.shape[1]
    n_samples  = data.shape[0]

    std_data = np.std(data, axis=0)
    rand_idx = np.random.randint(data.shape[0], size=n_class)

    for i in range(n_class):
        random_point = data[rand_idx[i]]
        mu.append(random_point)
        std.append(std_data)

    flag = True
    y    = np.zeros(shape=(n_samples))

    while(flag):
        print(1)
        print(std)
        a    = np.array([multivariate_normal.pdf(data, mu[i], std[i])
                             for i in range(n_class)])
        a    = a.T
        print(a)
        e    = np.array([np.argmin(z) for z in a])
        print(e)
        flag = (np.any(y - e))
        y    = e

        for i in range(n_class):
            t = [data[j] for j in range(n_class) if (y[j] == i)]
            mu.append(np.mean(t, axis=0))
            std.append(np.mean(t, axis=0))

    return (y, mu, std)

def classify(data, n_class):
    y, mu, std = em_normal(data, n_class)
    return y

def get_params(data, n_class):
    y, mu, std = em_normal(data, n_class)
    return (mu, std)
