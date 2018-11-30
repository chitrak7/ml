from librosa import load, get_duration
import numpy as np
import os

def load_audio_file(musicFile, sr=22050):
    breakInterval = 3600
    segLength     = 1
    data          = []

    audioDuration = get_duration(filename=musicFile) // 1.0
    numSegments   = int(audioDuration // breakInterval)

    for i in range(numSegments):
        st      = time.time()
        offset  = i * breakInterval
        y , srp = load(musicFile, sr=sr, duration=breakInterval, offset=offset, res_type='kaiser_fast' )
        if (i==0):
            data = y
        else:
            data    = data + y

    offset   = numSegments * breakInterval
    duration = audioDuration - offset
    y , srp  = load(musicFile, sr=sr, duration=duration, offset=offset, res_type='kaiser_fast' )
    if(len(data)==0):
        data = y
    else:
        data     = data + y

    return data

def load_video_file(videoFile, sr):
    audioFile      = "audio.wav"
    command_string = "ffmpeg -i " + videoFile + " " + audioFile
    os.system(command_string)

    data = load_audio_file(audioFile, sr)

    os.delete(audioFile)
    return data
