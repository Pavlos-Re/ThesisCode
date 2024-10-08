import keras
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib
import text

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import librosa
import librosa.display
from IPython.display import Audio
import warnings

warnings.filterwarnings('ignore')
from datasets import load_dataset
from transformers import pipeline
import pandas as pd
import plotly.express as px
from moviepy.editor import AudioFileClip


def convert_to_to_wav(input_file, output_file):
    try:
        # Load the WAV audio file
        clip = AudioFileClip(input_file)

        # Write the audio clip to an MP3 file
        clip.write_audiofile(output_file, codec='pcm_mulaw')

        print(f"Conversion successful! MP3 file saved as: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


def run():
    paths = []
    labels = []

    for dirname, _, filenames in os.walk('audio_samples'):
        for filename in filenames:
            paths.append(os.path.join(dirname, filename))
            label = filename.split('_')[-1]
            label = label.split('.')[0]
            labels.append(label.lower())
        if len(paths) == 2800:
            break

    print('Dataset is Loaded')

    print(len(paths))

    print(paths[:5])

    print(labels[:5])

    df = pd.DataFrame()
    df['speech'] = paths
    df['label'] = labels
    print(df.head())

    print(df['label'].value_counts())

    #
    # sns.countplot(data=df, x='label')
    #
    #
    # def waveplot(data, sr, emotion):
    #     plt.figure(figsize=(10, 4))
    #     plt.title(emotion, size=20)
    #     librosa.display.waveshow(data, sr=sr)
    #     plt.show()
    #
    #
    # def spectogram(data, sr, emotion):
    #     x = librosa.stft(data)
    #     xdb = librosa.amplitude_to_db(abs(x))
    #     plt.figure(figsize=(11, 4))
    #     plt.title(emotion, size=20)
    #     librosa.display.specshow(xdb, sr=sr, x_axis='time', y_axis='hz')
    #     plt.colorbar()
    #
    # emotion = 'fear'
    # path = np.array(df['speech'][df['label']==emotion])[0]
    # data, sampling_rate = librosa.load(path)
    # waveplot(data, sampling_rate, emotion)
    # spectogram(data, sampling_rate, emotion)
    #
    # emotion = 'angry'
    # path = np.array(df['speech'][df['label']==emotion])[1]
    # data, sampling_rate = librosa.load(path)
    # waveplot(data, sampling_rate, emotion)
    # spectogram(data, sampling_rate, emotion)
    # Audio(path)
    #
    # emotion = 'disgust'
    # path = np.array(df['speech'][df['label']==emotion])[0]
    # data, sampling_rate = librosa.load(path)
    # waveplot(data, sampling_rate, emotion)
    # spectogram(data, sampling_rate, emotion)
    # Audio(path)
    #
    # emotion = 'neutral'
    # path = np.array(df['speech'][df['label']==emotion])[0]
    # data, sampling_rate = librosa.load(path)
    # waveplot(data, sampling_rate, emotion)
    # spectogram(data, sampling_rate, emotion)
    # Audio(path)
    #
    #
    # emotion = 'sad'
    # path = np.array(df['speech'][df['label']==emotion])[0]
    # data, sampling_rate = librosa.load(path)
    # waveplot(data, sampling_rate, emotion)
    # spectogram(data, sampling_rate, emotion)
    # Audio(path)
    #
    #
    # emotion = 'ps'
    # path = np.array(df['speech'][df['label']==emotion])[0]
    # data, sampling_rate = librosa.load(path)
    # waveplot(data, sampling_rate, emotion)
    # spectogram(data, sampling_rate, emotion)
    # Audio(path)
    #
    # emotion = 'happy'
    # path = np.array(df['speech'][df['label']==emotion])[0]
    # data, sampling_rate = librosa.load(path)
    # waveplot(data, sampling_rate, emotion)
    # spectogram(data, sampling_rate, emotion)
    # Audio(path)

    def extract_mfcc(filename):
        y, sr = librosa.load(filename, duration=3, offset=0.5)
        mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
        return mfcc

    X_mfcc = df['speech'].apply(lambda x: extract_mfcc(x))

    X = [x for x in X_mfcc]
    X = np.array(X)

    X = np.expand_dims(X, -1)

    from sklearn.preprocessing import OneHotEncoder
    enc = OneHotEncoder()
    y = enc.fit_transform(df[['label']])

    y = y.toarray()

    from keras.src.models import Sequential
    from keras.src.layers import Dense, LSTM, Dropout

    model = Sequential([
        LSTM(256, return_sequences=False, input_shape=(40, 1)),
        Dropout(0.2),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(7, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()

    history = model.fit(X, y, validation_split=0.2, epochs=50, batch_size=64)

    epochs = list(range(50))

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    plt.plot(epochs, loss, label='train loss')
    plt.plot(epochs, val_loss, label='val loss')
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.legend()
    plt.show()

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    plt.plot(epochs, acc, label='train accuracy')
    plt.plot(epochs, val_acc, label='val accuracy')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    plt.legend()
    plt.show()

    # Save the model
    model.save('emotion_recognition_model.h5')

    # Load the model
    model = keras.models.load_model('emotion_recognition_model.h5')

    # Define function to predict emotion from an audio file
    def predict_emotion(audio_path):
        mfcc = extract_mfcc(audio_path)
        mfcc = np.expand_dims(mfcc, axis=0)
        mfcc = np.expand_dims(mfcc, axis=-1)
        prediction = model.predict(mfcc)
        predicted_emotion = enc.inverse_transform(prediction)[0][0]
        return predicted_emotion

    input_file = 'audio.wav'
    output_file = 'audio2.wav'
    #output_file = 'audio.wav'
    convert_to_to_wav(input_file, output_file)

    # Test the model with a new audio file
    test_audio_path = output_file
    predicted_emotion = predict_emotion(test_audio_path)
    print(f'The predicted emotion for the test audio is: {predicted_emotion}')

    return predicted_emotion

# if __name__ == "__main__":
#     run()
