import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

def mle_normal(data):
    n   = data.shape[0]
    m   = data.shape[1]
    mu  = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (n, mu, std)

def log_likelihood(data, mu, std):
    ll = 0
    y = multivariate_normal.pdf(data, mean=mu, cov=std);
    for yp in y:
        ll += np.log(yp)
    return ll

def BIC(a,b):
    na, mua, stda = mle_normal(a)
<<<<<<< HEAD
    nb, mub, stdb = mle_normal(b)
=======
    na, mua, stda = mle_normal(b) # shouldn't this nb,mub, stdb
>>>>>>> 7048973fb3518f8f8805b27bd717a9c81fd7b839

    c             = np.concatenate((a, b), axis=0)
    nc, muc, stdc = mle_normal(c)
    lla           = log_likelihood(a, mua, stda)
    llb           = log_likelihood(b, mub, stdb)
    llc           = log_likelihood(c, muc, stdc)

    return (llc - lla - llb)/nc

def speaker_change(data, window_size):
    data = np.array(data)
    threshold = -15

    y = []
    n_windows = data.shape[0]

    for i in range(n_windows-1):
        y.append(BIC(data[i], data[i+1]))

    change = [(i<threshold) for i in y]
    print([(i) for i in y if (i<threshold)])
    time   = [(i+1) for i in range(len(change)) if change[i]]

    return np.array(time)
