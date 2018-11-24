import numpy as np
import speaker_change

def mle_normal(data):
    n   = data.shape[0]
    m   = data.shape[1]
    mu  = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (n, mu, std)

def log_likelihood(data, mu, std):
    ll = 0
    y = multivariate_normal.pdf(x, mean=mu, cov=std);
    for yp in y:
        ll += np.log(yp)
    return ll

def BIC(a,b):
    na, mua, stda = mle_normal(a)
    na, mua, stda = mle_normal(b)

    c             = a + b
    nc, muc, stdc = mle_normal(c)
    lla           = log_likelihood(a, mua, stda)
    llb           = log_likelihood(b, mub, stdb)
    llc           = log_likelihood(c, muc, stdc)

    return (llc - lla - llb)/nc

def speaker_diarization(data, window_size):
    threshold = 0.1
    changes   = speaker_change.speaker_change(data, window_size)

    segments = [(0, changes[0])]
    for i in range(changes.shape[0]-1):
        segments.append((changes[i], changes[i+1]))
    segments.append((changes[-1], data.shape[0]))

    speaker1 = []
    for i in np.arange(segments[0][0], segments[0][1]):
        for j in data[i]:
            speaker1.append(j)

    speakers = [speaker1]

    for segment in segments[1:]:
        t = threshold
        j = -1

        speaker = []
        for i in np.arange(segment[0], segment[1]):
            for k in data[i]:
                speaker.append(k)

        for i in range(len(speakers)):
            bic = BIC(speakers[i], speaker)
            if(bic < t):
                j = i
                t = bic

        if(j==-1):
            speakers.append(speaker)
        else:
            for k in speaker:
                speakers[j].append(k)

    return speakers
