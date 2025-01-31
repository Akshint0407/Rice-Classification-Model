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
        .popup {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 300px;
            background-color: rgba(0, 0, 0, 0.9); /* Black background */
            border-radius: 10px;
            padding: 20px;
            z-index: 1000;
            color: white; /* White text */
        }}
        .popup h4 {{
            margin-top: 0;
        }}
        .button-container {{
            position: absolute;
            top: 10px;
            right: 10px;
        }}
        .button {{
            background-color: rgba(255, 255, 255, 0.7); /* Semi-transparent button */
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            cursor: pointer;
            margin-left: 5px; /* Space between buttons */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Replace with your new static image URL
add_background("https://media.gettyimages.com/id/922610806/video/abstract-digital-background-loopable-4k.jpg?s=640x640&k=20&c=gMhuPvcRIjfk-NYH0y1jEVwqnmLm2jpFk4NDS1PalVU=")

# Streamlit app title
st.title("🌾 Rice Classification Model 🌾")

# Initialize session state for popups
if 'show_instruction' not in st.session_state:
    st.session_state.show_instruction = False
if 'show_about' not in st.session_state:
    st.session_state.show_about = False
if 'show_login' not in st.session_state:
    st.session_state.show_login = False

# Function to toggle popups
def toggle_instruction():
    st.session_state.show_instruction = not st.session_state.show_instruction

def toggle_about():
    st.session_state.show_about = not st.session_state.show_about

def toggle_login():
    st.session_state.show_login = not st.session_state.show_login

# Add buttons for instruction and about popups in top right corner
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("📖 Instructions"):
        toggle_instruction()
with col2:
    if st.button("ℹ️ About"):
        toggle_about()
with col3:
    if st.button("🔑 Login"):
        toggle_login()

# Display Instruction Popup if activated
if st.session_state.show_instruction:
    st.markdown(
        f"""
        <div class="popup">
            <h4>How to Use This App</h4>
            <p>1. Read the instructions Carefully!</p>
            <p>2. Input the required features in the fields provided.</p>
            <p>3. Click the "🔮 Predict" button to get the classification result.</p>
            <p>4. Check the prediction displayed below.</p>
            <p>5. To activate and deactivate the popups, click the button itself and ignore the X button.</p>
            <button onclick="window.streamlitSessionState.set('show_instruction', false);" style="float:right; background-color: red; color: white; border: none; border-radius: 5px; padding: 5px 10px;">X</button>
        </div>
        """,
        unsafe_allow_html=True
    )

# Display About Popup if activated
if st.session_state.show_about:
    st.markdown(
        """
        <div class="popup">
            <h4>About This App</h4>
            <p>This app predicts rice varieties based on various input features.</p>
            <p>It uses a machine learning model trained on rice classification data.</p>
            <p>Applications include agricultural research and crop management.</p>
            <button onclick="window.streamlitSessionState.set('show_about', false);" style="float:right; background-color: red; color: white; border: none; border-radius: 5px; padding: 5px 10px;">X</button>
        </div>
        """,
        unsafe_allow_html=True
    )

# Display Login Popup if activated
if st.session_state.show_login:
    st.markdown(
        """
        <div class="popup">
            <h4>😂 Why do you need to log in?</h4>
            <p>Just put the values and forget the login!</p>
            <button onclick="window.streamlitSessionState.set('show_login', false);" style="float:right; background-color: red; color: white; border: none; border-radius: 5px; padding: 5px 10px;">X</button>
        </div>
        """,
        unsafe_allow_html=True
    )

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
        result_message = "The predicted class is **Cammeo**! 🌾"
    else:
        result_message = "The predicted class is **Osmancik**! 🌾"

    # Display a custom message without background color
    st.markdown(f"<h3 style='color: white;'>🎊 Congratulations! {result_message} 🎊</h3>", unsafe_allow_html=True)