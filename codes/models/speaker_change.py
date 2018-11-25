import numpy as np
from scipy.stats import multivariate_normal
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
    na, mua, stda = mle_normal(b) # shouldn't this nb,mub, stdb

    c             = a + b
    nc, muc, stdc = mle_normal(c)
    lla           = log_likelihood(a, mua, stda)
    llb           = log_likelihood(b, mub, stdb)
    llc           = log_likelihood(c, muc, stdc)

    return (llc - lla - llb)/nc

def speaker_change(data, window_size):
    threshold = 0.1

    y = []
    n_windows = data.shape[0]

    for i in range(n_windows-1):
        y.append(BIC(data[i], data[i+1]))

    change = [(i>threshold) for i in y]
    time   = [(i+1) for i in range(len(change)) if change[i]]

    return np.array(time)
