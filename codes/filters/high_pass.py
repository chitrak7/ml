import librosa
import numpy as np
from scipy.signal import butter, lfilter

Class Mfcc_Filter:
    def __init__(self, window_size, cutoff=250, order=5):
        self.window_len = window_len
        self.cutoff     = cutoff
        self.order      = order

    def filter(self, y, sr):
        window_size = self.window_size
        sample_size = window_size *  sr
        cutoff      = self.cutoff
        order       = self.order

        nyq         = 0.5 * sr
        high        = cutoff/nyq

        n_sample = y.shape[0] // sample_size
        data = []

        for i in range(n_sample):
            start = i*sample_size
            end   = start + sample_size
            yp    = y[start:end]

            b, a  = butter(order, high, 'high',  btype='band')
            yp    = lfilter(b, a, yp)
            yp    = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
            yp    = yp.T

            data.append(yp)

        return data
