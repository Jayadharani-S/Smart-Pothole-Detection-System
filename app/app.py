import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile

st.set_page_config(page_title="Pothole Detection System")

st.title("🚧 Pothole Detection using YOLOv8")
st.write("Upload a road image to check for potholes.")

# Load model once
model = YOLO("../model/best.pt")

uploaded_file = st.file_uploader("Upload Road Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.image(uploaded_file, caption="Uploaded Image", width='stretch')

    # Run prediction
    results = model(temp_path)

    boxes = results[0].boxes

    if boxes is not None and len(boxes) > 0:
        st.error("⚠️ Pothole detected on the road!")
    else:
        st.success("✅ No potholes detected. Road looks safe!")

    # Show result image with boxes
    result_img = results[0].plot()
    st.image(result_img, caption="Detection Result", width='stretch')