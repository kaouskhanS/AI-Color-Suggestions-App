import streamlit as st
from PIL import Image
import numpy as np
import json
import cv2

from utils import crop_face, extract_skin, get_dominant_color, classify_season, detect_face_mtcnn

# Load color palettes
with open("palettes.json") as f:
    palettes = json.load(f)

st.title("AI Face Recognition & Dress Color Suggestion")

mode = st.radio("Choose Input Method:", ["Upload Photo", "Capture Photo"])

img = None

if mode == "Upload Photo":
    uploaded = st.file_uploader("Upload a clear face photo:", type=["jpg", "jpeg", "png"])
    if uploaded:
        img_pil = Image.open(uploaded).convert("RGB")
        img = np.array(img_pil)

elif mode == "Capture Photo":
    picture = st.camera_input("Take a photo")
    if picture:
        img_pil = Image.open(picture)
        img = np.array(img_pil)
elif mode == "Capture Photo":
    picture = st.camera_input("Take a photo")
    if picture:
        img_pil = Image.open(picture)
        img = np.array(img_pil)


# If we have an image, proceed with processing
if img is not None:
    st.image(img, caption="Input", use_column_width=True)
    face_bbox = detect_face_mtcnn(img)
    if face_bbox:
        face_img = crop_face(img, face_bbox)
        skin_img = extract_skin(face_img)
        dominant_color = get_dominant_color(skin_img)
        st.markdown("**Detected skin tone:**")
        st.image(np.ones((50, 200, 3), dtype='uint8') * np.array(dominant_color, dtype='uint8'), width=200)
        season = classify_season(dominant_color)
        st.success(f"Suggested palette: {season}")
        st.markdown("**Recommended Dress Colors:**")
        st.write(", ".join(palettes[season]))
    else:
        st.warning("No face detected. Please try another input.")
