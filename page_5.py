import openai
import os
import openai
import streamlit as st
import requests
from openai import OpenAI
from pathlib import Path

st.markdown("# Page 5 Text to Speech ❄️")
st.sidebar.markdown("# Page 5 Text to Speech ❄️")

speech_file_path = Path(__file__).parent / "newfile.mp3"

#openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key="OPENAI_API_KEY") 

def text_to_speech(text,path):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text
    )
    response.stream_to_file(speech_file_path)

def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Your job is to help help keep track of and give suggestions/recommendations based on user input/data."},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

# Create a text input field
text = st.text_input('Enter the reminders/suggestions you would like to listen to')

# Create a button
if st.button('Submit'):
    st.write(text_to_speech(get_completion(text), speech_file_path))
    #text_to_speech(text, speech_file_path)

    audio_file = open(speech_file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
