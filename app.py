import streamlit as st
import pandas as pd
import joblib
import time  # Import time for simulating processing delay

# Load the saved model and scaler
model = joblib.load('grid_classifier.pkl')
scaled = joblib.load('scaled1.pkl')

# Set the page configuration
st.set_page_config(page_title="Rice Classification Model", layout="wide")

# Add a background image
def add_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
            background-position: center;
            color: white;  /* Change text color to white for better visibility */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Replace with your image URL or path
add_background("https://e1.pxfuel.com/desktop-wallpaper/99/166/desktop-wallpaper-black-and-red-abstract-high-definition-413.jpg")

# Streamlit app title
st.title("🌾 Rice Classification Model 🌾")

# Input fields with better layout
st.header("Input Features")
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area", min_value=0.0)
    perimeter = st.number_input("Perimeter", min_value=0.0)
    major_axis_length = st.number_input("Major Axis Length", min_value=0.0)
    eccentricity = st.number_input("Eccentricity", min_value=0.0)

with col2:
    minor_axis_length = st.number_input("Minor Axis Length", min_value=0.0)
    convex_area = st.number_input("Convex Area", min_value=0.0)
    extent = st.number_input("Extent", min_value=0.0)

# Create a DataFrame from inputs
input_data = {
    'Area': area,
    'Perimeter': perimeter,
    'Major_Axis_Length': major_axis_length,
    'Minor_Axis_Length': minor_axis_length,
    'Eccentricity': eccentricity,
    'Convex_Area': convex_area,
    'Extent': extent
}
input_df = pd.DataFrame([input_data])

# Scale the input data
scaled_input = scaled.transform(input_df)

# Predict button with loading animation
if st.button("🔮 Predict"):
    with st.spinner('Processing...'):
        time.sleep(1)  # Simulate some processing time (optional)
        prediction = model.predict(scaled.transform(scaled_input))

    # Display results after processing is complete
    st.subheader("🎉 Prediction 🎉")
    
    if prediction[0] == 0:
        result_message = "The predicted class is Cammeo! 🌾"
    else:
        result_message = "The predicted class is Osmancik! 🌾"

    # Display a custom message without background color
    st.markdown(f"<h3 style='color: white;'>🎊 Congratulations! {result_message} 🎊</h3>", unsafe_allow_html=True)
