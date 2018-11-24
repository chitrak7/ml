import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import classifiers.EM_normal as km
y, sr = librosa.load("../data/panel1.mp3", duration=100)

D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
print(D.shape)

y = km.classify(D.T, 5)

plt.plot(y, 'g.')


plt.show()
