from librosa import load, get_duration
from librosa.feature import mfcc
import numpy as np
from keras.models import load_model, Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Convolution2D, MaxPooling2D
from keras.optimizers import Adam

def speech_detection(data, model, window_size):
    data   = np.array([np.mean(i, axis=0) for i in data])
    model  = load_model(model)
    result = np.argmax(model.predict(data), axis=1)
    return np.array([[i] for i in range(len(result)) if (result[i]==0)]).flatten()

def train_speech_detection_model(data, labels, window_size, target):
    data   = np.array([np.mean(i, axis=0) for i in data])
    lb = LabelEncoder()
    split   = (data.shape[0]*3)//10
    vdata   = data[split:]
    vLabels = labels[split:]
    data    = data[:split]
    labels  = labels[:split]
    labels  = keras.utils.to_categorical(lb.fit_transform(labels))
    vLabels = keras.utils.to_categorical(lb.fit_transform(vLabels))

    # build model
    model = Sequential()

    model.add(Dense(256, input_shape=(data.shape[1],)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(2))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
    model.fit(data,labels, batch_size=128, epochs=1000, validation_data=(vdata, vLabels))

    model.save(modelFile)
