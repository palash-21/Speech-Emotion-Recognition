import streamlit as st
import pandas as pd
import numpy as np
import librosa
from keras.models import load_model
from pydub import AudioSegment
import os

def audio_converter(file):
    if file.name.split('.')[1] == "mp3" :
        st.write('Converting mp3 to wav...')
        sound = AudioSegment.from_mp3(file)
        new_file = file.name.split('.')[0] + ".wav"
        sound.export(new_file, format="wav")
    else :
        new_file = file
    
    return new_file

def extract_features_audio(data):
	result = np.array([])
	zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
	result=np.hstack((result, zcr)) # stacking horizontally

    # Chroma_stft
	stft = np.abs(librosa.stft(data))
	chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
	result = np.hstack((result, chroma_stft)) # stacking horizontally

    # MFCC
	mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
	result = np.hstack((result, mfcc)) # stacking horizontally

    # Root Mean Square Value
	rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
	result = np.hstack((result, rms)) # stacking horizontally

    # MelSpectogram
	mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
	result = np.hstack((result, mel)) # stacking horizontally

	return result

def emotion_decoder(prediction):
    list_pred = pred.tolist()
    emotion_list = ['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']
    emotion_dict = dict(zip(emotion_list,list_pred[0]))
    pred_emotion = ''
    for emot,pred_val in emotion_dict.items():
        max_pred = max(list_pred[0])
        if pred_val==max_pred:
            pred_emotion = emot
    return pred_emotion

modelfile = 'model/model_1.h5'    

model = load_model(modelfile)

st.title('Speech Emotion Recognition')

uploaded_file = st.file_uploader("Upload Files",type=['wav','mp3'])
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)
    st.audio(uploaded_file, format="audio/wav", start_time=0)
    wave_file = audio_converter(uploaded_file)
    st.write('Recognizing emotion in your speech...')
    data, sample_rate = librosa.load(wave_file, duration=2.5, offset=0.6)
    try :
        os.remove(wave_file)
    except :
        pass
    fea = np.array(extract_features_audio(data))
    fea = fea.reshape((-1,162))
    fea = pd.DataFrame(fea)
    fea.reset_index(inplace=True)
    fea = np.array(fea)
    fea = np.expand_dims(fea, axis=2)

    pred = model.predict(fea)		

    emotion = emotion_decoder(pred)
   
    st.write(f'The uploaded audio has the following emotion:"{emotion}"')
