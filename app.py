import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="AI Watermark Remover", layout="centered")

st.title("✨ AI Watermark Remover")
st.write("Upload an image and draw over the watermark to remove it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_column_width=True)
    
    st.info("Logic for AI processing will be connected in the next step!")
    
    if st.button('Clean Image'):
        st.success("Ready to process!")
      
