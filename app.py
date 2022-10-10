import streamlit as st

start = st.slider("Start time", min_value=0, max_value=100, value=0)

audio_file = open("audio//22228723.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mp3", start_time=start)
