# VisionQuery AI — Upload an image and ask natural-language questions about it

import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv
from google import genai

# Load Environment Variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY not found. Please set it in a .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

# Gemini Call
def get_gemini_response(prompt, image):
    if prompt:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt, image],
        )
    else:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=image,
        )
    return response.text

# Streamlit UI
st.set_page_config(page_title="VisionQuery AI", layout="centered")

st.title("VisionQuery AI")
st.caption("Upload an image and ask natural-language questions about it.")

prompt = st.text = st.text_input("Ask something about the image:")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Analyze Image")

# Interaction Logic 
if submit:
    if image is None:
        st.warning("Please upload an image before asking a question.")
    else:
        with st.spinner("Analyzing..."):
            response = get_gemini_response(prompt, image)

        st.subheader("AI Insight")
        st.write(response)
