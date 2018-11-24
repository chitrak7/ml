import numpy as np

def distance(a, b):
    t = a-b
    return np.linalg.norm(t)

def kmeans(data, n_class):
    mu    = []

    n_features = data.shape[1]
    n_samples  = data.shape[0]

    rand_idx = np.random.randint(data.shape[0], size=n_class)

    for i in range(n_class):
        random_point = data[rand_idx[i]]
        mu.append(random_point)

    flag = True
    y    = np.zeros(shape=(n_samples))

    while(flag):
        e    = np.array([np.argmin([distance(x, mu[i])
                             for i in range(n_class)]) for x in data])

        flag = (np.any(y - e))
        y    = e

        for i in range(n_class):
            t = [data[j] for j in range(n_class) if (y[j] == i)]
            mu.append(np.mean(t, axis=0))

    return (y, mu)

def classify(data, n_class):
    y, mu = kmeans(data, n_class)
    return y

def get_params(data, n_class):
    y, mu = kmeans(data, n_class)
    return mu
