import librosa
import numpy as np

class Mfcc_Filter:
    def __init__(self, window_size, n_mfcc=40):
        self.window_size = window_size
        self.n_mfcc      = n_mfcc

    def filter(self, y, sr):
        window_size = self.window_size
        sample_size = int(window_size *  sr)
        n_mfcc      = self.n_mfcc

        n_sample = int(y.shape[0] // sample_size)
        data = []

        for i in range(n_sample):
            start = i*sample_size
            end   = start + sample_size
            yp    = y[start:end]

            mfcc  = librosa.feature.mfcc(yp, sr=sr, n_mfcc=n_mfcc)
            mfcc  = mfcc.T

            data.append(mfcc)

        return data
