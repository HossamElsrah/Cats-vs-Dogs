# Import required libraries
import streamlit as st 
from PIL import Image 
import numpy as np  
import tensorflow as tf 
import os

MODEL_PATH = 'https://github.com/HossamElsrah/Cats-vs-Dogs/blob/main/dogs_vs_cats_model.h5'
if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found at: {os.path.abspath(MODEL_PATH)}")
    st.stop()

@st.cache_resource  
def load_model():
    try:
        
        with tf.keras.utils.custom_object_scope({}):
            return tf.keras.models.load_model(MODEL_PATH, compile=False)
    except Exception as e:
        st.error(f"Failed to load model: {str(e)}")
        return None

model = load_model()

if model is None:
    st.stop()

# Configure the web app interface
st.title('🐱 Cat vs Dog Classifier 🐶')
st.write("Upload an image for classification")

# Create file uploader widget
uploaded_file = st.file_uploader(
    "Choose an image...", 
    type=["jpg", "png", "jpeg"],  
    help="Select a clear image of either a cat or dog"  
)

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)  # تعديل بسيط هنا
    
    # Preprocess the image for model input
    img = image.resize((150, 150)) 
    img_array = np.array(img)  # Convert to numpy array
    img_array = img_array / 255.0  # Normalize pixel values (0-1)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction
    prediction = model.predict(img_array)
    confidence = max(prediction[0][0], 1 - prediction[0][0])  # Calculate confidence
    
    # Display results
    if prediction[0][0] > 0.5:
        st.success(f'Prediction: Dog 🐶 (Confidence: {confidence*100:.1f}%)')
    else:
        st.success(f'Prediction: Cat 🐱 (Confidence: {confidence*100:.1f}%)')
