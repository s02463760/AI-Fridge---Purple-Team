import os
import openai
import streamlit as st
from openai import OpenAI


st.markdown("#Feature 1: Text Generation ❄️")
st.sidebar.markdown("# Feature 1: Text Generation ❄️")

#openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key="OPENAI_API_KEY") 

# create a wrapper function
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

# create our streamlit app
with st.form(key = "chat"):
    prompt = st.text_input("Hello, how can I help you today? ") 
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))
