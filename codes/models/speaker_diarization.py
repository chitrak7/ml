import numpy as np
import models.speaker_change as sc
from scipy.stats import multivariate_normal

def mle_normal(data):
    data = np.array(data)
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
    nb, mub, stdb = mle_normal(b)

    c             = a + b
    nc, muc, stdc = mle_normal(c)
    lla           = log_likelihood(a, mua, stda)
    llb           = log_likelihood(b, mub, stdb)
    llc           = log_likelihood(c, muc, stdc)

    return (llc - lla - llb)/nc

def speaker_diarization(data, window_size):
    data = np.array(data)
    threshold = -12
    changes   = sc.speaker_change(data, window_size)

    segments = [(0, changes[0])]
    for i in range(changes.shape[0]-1):
        segments.append((changes[i], changes[i+1]))
    segments.append((changes[-1], data.shape[0]))

    speaker1 = []
    for i in np.arange(segments[0][0], segments[0][1]):
        for j in data[i]:
            speaker1.append(j)

    speakers = [speaker1]
    timeframe = [[(segments[0][0]*window_size, segments[0][1]*window_size)]]
    for segment in segments[1:]:
        t = threshold
        j = -1

        speaker = []
        for i in np.arange(segment[0], segment[1]):
            for k in data[i]:
                speaker.append(k)

        for i in range(len(speakers)):
            bic = BIC(speakers[i], speaker)
            if(bic > t):
                j = i
                t = bic

        if(j==-1):
            speakers.append(speaker)
            timeframe.append([(segment[0]*window_size, segment[1]*window_size)])
        else:
            timeframe[j].append((segment[0]*window_size, segment[1]*window_size))
            for k in speaker:
                speakers[j].append(k)


    return timeframe
