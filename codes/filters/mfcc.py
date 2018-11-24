import librosa
import numpy as np

Class Mfcc_Filter:
    def __init__(self, window_size, n_mfcc=40):
        self.window_len = window_len
        self.n_mfcc     = n_mfcc

    def filter(self, y, sr):
        window_size = self.window_size
        sample_size = window_size *  sr
        n_mfcc      = self.n_mfcc

        n_sample = y.shape[0] // sample_size
        data = []

        for i in range(n_sample):
            start = i*sample_size
            end   = start + sample_size
            yp    = y[start:end]

            mfcc  = librosa.mfcc(yp, sr=sr, n_mfcc=n_mfcc)
            mfcc  = mfcc.T

            data.append(mfcc)

        return data
