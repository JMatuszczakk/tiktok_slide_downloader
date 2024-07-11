import streamlit as st
from main import download

st.title("TikTok Slideshow downloader")

with st.form(key='my_form'):
    tiktok_url = st.text_input(label='Enter TikTok URL')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    with st.spinner('Downloading images...'):
        rint = download(tiktok_url)