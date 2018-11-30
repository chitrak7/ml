import librosa
from sklearn.decomposition import PCA
import numpy as np
from scipy.signal import butter, lfilter

class Band_Pass:
    def __init__(self, window_size, high=600, low=50, order=5):
        self.window_size = window_size
        self.high        = high
        self.low         = low
        self.order       = order

    def filter(self, y, sr):
        window_size = self.window_size
        sample_size = window_size *  sr
        high        = self.high
        low         = self.low
        order       = self.order

        nyq         = 0.5 * sr
        low_c       = low/nyq
        high_c      = high/nyq

        n_sample = y.shape[0] // sample_size
        data = []
        for i in range(n_sample):
            start = i*sample_size
            end   = start + sample_size
            yp    = y[start:end]

            b, a  = butter(order, [low_c, high_c],  btype='band')
            yp    = lfilter(b, a, yp)

            data.append(yp)

        data = np.array(data)
        print(data.shape)
        return data.flatten()
