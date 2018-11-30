import librosa
import numpy as np
from scipy.signal import butter, lfilter

class Low_Pass:
    def __init__(self, window_size, cutoff=100, order=5):
        self.window_size = window_size
        self.cutoff      = cutoff
        self.order       = order

    def filter(self, y, sr):
        window_size = self.window_size
        sample_size = window_size *  sr
        cutoff      = self.cutoff
        order       = self.order

        nyq         = 0.5 * sr
        low         = cutoff/nyq

        n_sample = y.shape[0] // sample_size
        data = []

        for i in range(n_sample):
            start = i*sample_size
            end   = start + sample_size
            yp    = y[start:end]

            b, a  = butter(order, low, 'low')
            yp    = lfilter(b, a, yp)


            data.append(yp)
        data=np.array(data)
        return data.flatten()
