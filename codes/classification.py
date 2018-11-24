import numpy as np
import models.EM_normal           as em
import models.kmeans              as km
import models.homomorphism        as hm
import models.speaker_diarization as sd
import models.speaker_change      as sc
import models.speech_detection    as sd
import filters.band_pass          as bp
import filters.low_pass           as lp
import filters.high_pass          as hp
import filters.mfcc               as mf
import utils.load_file            as lf

def classification(file, audio=True, filter, window_size=1, sr=22050):
    if(audio):
        data = lf.load_audio_file(file, sr)
    else:
        data = lf.load_video_file(file, sr)

    data = filter.filter(data, sr)
