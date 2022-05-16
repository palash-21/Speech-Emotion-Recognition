# Speech-Emotion-Recognition

I have used MLP Classifier, CNN , LSTM & LSTM-CNN networks for this task
 
Environments
Python 3.10
Keras
 

Project Structure:

![Project Structure](https://user-images.githubusercontent.com/76896938/168626223-ffbc81d5-24c1-49ec-9469-340a714f5fe1.png)


Datasets used:
1. CREMA-D
CREMA-D audio dataset for our task. CREMA-D is a data set of 7,442 original clips from 91 actors.
These clips were from 48 male and 43 female actors between the ages of 20 and 74 coming from a variety of races and ethnicities 
(African America, Asian, Caucasian, Hispanic, and Unspecified).

Actors spoke from a selection of 12 sentences. The sentences were presented using one of six different emotions 
(Anger, Disgust, Fear, Happy, Neutral, and Sad) and four different emotion levels (Low, Medium, High, and Unspecified).

2. TESS
TESS (Toronto Emotional Speech Set): 2 female speakers (young and old), 2800 audio files, random words were spoken in 7 different emotions.
These stimuli were modeled on the Northwestern University Auditory Test No. 6 (NU-6; Tillman & Carhart, 1966). 
A set of 200 target words were spoken in the carrier phrase 
"Say the word _____' by two actresses (aged 26 and 64 years) and recordings were made of the set portraying each of seven emotions
(anger, disgust, fear, happiness, pleasant surprise, sadness, and neutral). There are 2800 stimuli in total.

3. SAVEE
(Surrey Audio-Visual Expressed Emotion): 4 male speakers, 480 audio files, same sentences were spoken in 7 different emotions. 
Speakers- 'DC', 'JE', 'JK' and 'KL' are four male speakers recorded for the SAVEE database

Audio files consist of audio WAV files sampled at 44.1 kHz

There are 15 sentences for each of the 7 emotion categories. 
The initial letter(s) of the file name represents the emotion class, and the following digits represent the sentence number.
The letters 'a', 'd', 'f', 'h', 'n', 'sa' and 'su' represent 'anger', 'disgust', 'fear', 'happiness', 'neutral', 'sadness' and 'surprise' emotion classes respectively.

4. RAVDEES
RAVDESS: 2452 audio files, with 12 male speakers and 12 Female speakers, 
the lexical features (vocabulary) of the utterances are kept constant by speaking only 2 statements of equal lengths in 8 different emotions by all speakers.

Each of the 7356 RAVDESS files has a unique filename. The filename consists of a 7-part numerical identifier (e.g., 02-01-06-01-02-01-12.mp4). 
These identifiers define the stimulus characteristics:
Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised)

5. BERLIN
Berlin: Russian language: 5 male and 5 female speakers, 535 audio files, 10 different sentences were spoken in 7 different emotions. Emotion Codes:
W - Ärger (Wut) - anger
L - Langeweile - boredom
E - Ekel - disgust
A - Angst - fear
F - Freude - happy
T - Trauer - sad
N - - neutral

6. EMOVO
EMOVO-Italian Emotional Speech Dataset
It is a database built from the voices of up to 6 actors who played 14 sentences simulating 6 emotional states
(disgust, fear, anger, joy, surprise, sadness) plus the neutral state 6 professional actors were chosen, 3 male and 3 female.
Emotions: Italian and English translation
disgusto - disgust
gioia - joy
paura - fear
rabbia - anger
sorpresa - surprise
tristezza- sadness
stato emotivo neutro - neutral

7. CASIA
CASIA-Chinese Emotional Speech Corpus

Four professional speakers are required to utter 500 sentences which include 300 parallel texts and 200 non-parallel texts in six emotions.
There are 12,000 sentences in all which can be used in the research about emotional speech.
Emotions:
AA - angry NN - neutral HH - happy FF - fear SA - sad SS - surprise

8. SHEMO
Sharif Emotional Speech Database (ShEMO). The database includes 3000 semi-natural utterances, equivalent to 3 hours and 25 minutes of speech data extracted from online radio plays.
The ShEMO covers speech samples of 87 native-Persian speakers for five basic emotions including anger, fear, happiness, sadness and surprise, as well as neutral state.
The characters used in the label of the utterances and their corresponding meaning:
A: anger 
F: female speaker (if used at the beginning of the label e.g.F14A09) or fear (if used in the middle of the label e.g. M02F01)
H : happiness
M : male speaker\
N : neutral
S : sadness
W : surprise

9. CaFe
The Canadian French Emotional (CaFE) speech dataset contains six different sentences,
pronounced by six male and six female actors, in six basic emotions plus one neutral emotion. 
The six basic emotions are acted in two different intensities.
French            English translation
C = Colère        (Anger)
D = Dégoût        (Disgust)
J = Joie        (Happiness)
N = Neutre        (Neutral)
P = Peur        (Fear)
S = Surprise        (Surprise)
T = Tristesse        (Sadness)

10. AESDD
Acted Emotional Speech Dynamic Database -Greek

5 (3 female and 2 male) professional actors were recorded. 19 utterances of ambiguous out of context emotional content were chosen. Five emotions were chosen:

a (anger) d (disgust) f (fear) h (happiness) s (sadness)

11. JL corpus
This corpus was constructed by maintaining an equal distribution of 4 long vowels in New Zealand English.
File naming rule: (Gender)(speaker.ID)(Emotion)(Sentence.ID)(session.ID)
Default sample rate: 44100Hz
Encoding: 16 bit PCM

Data Augmnetation Technique used:
1. Noise Injection
2. Time shifting
3. Altering Pitch
4. Stretching

Audiio Features were extracted using Librosa:
1. ZCR   : Zero Crossing Rate
2. MFCC  : Mel Frequency Cepstrum Coefficients
3. MEL   : Mel-scaled spectrum
4. Croma : Chromagram
5. RMS   : Root Mean Square value

Best model : LSTM + CNN model
Model architecture:

![image](https://user-images.githubusercontent.com/76896938/168625682-8aae1610-6d2b-4939-8ba7-28a62df31ab5.png)

Deployed App on Azure:
Link: https://ser-streamlit.azurewebsites.net/

![image](https://user-images.githubusercontent.com/76896938/168626509-1b9d33c5-7cda-4c69-9181-a14e64c48a07.png)
