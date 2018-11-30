import numpy as np
import matplotlib.pyplot as plt
import librosa
from librosa.display import specshow
import models.EM_normal           as em
import models.kmeans              as km
import models.homomorphism        as hm
import models.speaker_diarization as sd
import models.speaker_change      as sc
import models.speech_detection    as sp
import filters.band_pass          as bp
import filters.low_pass           as lp
import filters.high_pass          as hp
import filters.mfcc               as mf
import utils.load_file            as lf

mfcc = mf.Mfcc_Filter(window_size=1)
def classification(file, filter, audio=True, window_size=1, sr=22050):
    if(audio):
        data = lf.load_audio_file(file, sr)
    else:
        data = lf.load_video_file(file, sr)

    data = filter.filter(data, sr)
    speech_idx = sp.speech_detection(data, "model.h5", window_size)
    speech = [data[i] for i in speech_idx]
    ts     = [(i,speech_idx[i]) for i in range(speech_idx.shape[0])]
    change = sd.speaker_diarization(speech, window_size)
    speakers = []
    ct = 1

    for i in range(len(change)):
        speakers.append([])
        speakers[i].append([])
        speakers[i].append([])
        tuple = change[i]
        if(len(tuple)<=3):
            continue
        for j in tuple:
            for k in np.arange(j[0], j[1]):
                speakers[i][0].append(k)
                speakers[i][1].append(ct)
        ct += 1
        plt.scatter(speakers[i][0], speakers[i][1])
    plt.show()
    print(change)

classification("../data/panel1.mp3", mfcc)
