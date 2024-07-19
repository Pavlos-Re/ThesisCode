import keras
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib
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

paths = []
labels = []
for dirname, _, filenames in os.walk('/home/pavlos/Desktop/test'):
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

sns.countplot(data=df, x='label')

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
    LSTM(256, return_sequences=False, input_shape=(40,1)),
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

# Test the model with a new audio file
test_audio_path = '/home/pavlos/Desktop/test3.wav'
predicted_emotion = predict_emotion(test_audio_path)
print(f'The predicted emotion for the test audio is: {predicted_emotion}')


model_writen = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

#sentences = ["Lately, I’ve been feeling like there’s no point in anything. Every day feels like a struggle, and I’m constantly overwhelmed by feelings of sadness and hopelessness. It’s like a heavy weight that I can’t shake off, no matter what I do. I often think about how things would be if I weren’t here. The thought of disappearing, of not having to deal with this pain anymore, is becoming more and more appealing. I wonder if anyone would really miss me, or if my absence would even be noticed. It feels like I’m just a burden to everyone around me. When I look in the mirror, all I see is failure. I can’t seem to do anything right, and the future looks so bleak. It’s hard to imagine things ever getting better. I try to reach out to people, but it feels like they don’t really understand what I’m going through. Sometimes, I think it would be easier for everyone if I just wasn’t here. I’ve been thinking about how I would do it. The thoughts come and go, but they’re getting more frequent and more detailed. It scares me, but it also feels like a solution to this never-ending pain. I know I need help, but it’s hard to ask for it. Admitting how I feel seems like it would just add to my sense of failure and disappointment. Every day is a battle to get through. I’m tired of fighting, tired of pretending that everything is okay. The thought of ending it all feels like a way to find peace, a way to stop the constant pain. I know there are people who care about me, but right now, it’s hard to see beyond this darkness."]

sentences = ["Only you can glue my blue and, Broken, shattered, battered porcelain heart, Tear my soul apart, So dark from smoking poison, Toxic, tainted love, Murder when from you is something holy, Only pure, so beautiful, When she sinks her teeth in me my flesh is red, And I bled out for us, Even hate from you would have me thankful, Only to be in your thoughts, Lonely in your arms, Lonely in your arms, In this violent dawn, Something feels so wrong"]

#sentences = ["I don't want to live like that anymore."]

model_outputs = model_writen(sentences)

print(model_outputs[0])