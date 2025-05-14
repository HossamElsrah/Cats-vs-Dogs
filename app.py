# Import required libraries
import streamlit as st 
from PIL import Image 
import numpy as np  
import tensorflow as tf 

# Cache the model loading to avoid reloading on every interaction
@st.cache_resource  
def load_model():
    """Load and return the pre-trained Keras model"""
    return tf.keras.models.load_model('dogs_vs_cats_model.h5')  

# Load the model
model = load_model()

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
