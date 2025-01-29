import streamlit as st
import pandas as pd
import pickle
import joblib

# Load the saved model and scaler
model = joblib.load('grid_classifier.pkl')
scaled = joblib.load('scaled1.pkl')


# Streamlit app
st.title("Rice Classification Model")

# Input fields
st.header("Input Features")
area = st.number_input("Area", min_value=0.0)
perimeter = st.number_input("Perimeter", min_value=0.0)
major_axis_length = st.number_input("Major Axis Length", min_value=0.0)
minor_axis_length = st.number_input("Minor Axis Length", min_value=0.0)
eccentricity = st.number_input("Eccentricity", min_value=0.0)
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

# Predict button
if st.button("Predict"):
    prediction = model.predict(scaled.transform(scaled_input))

    # Display results
    st.subheader("Prediction")
    if prediction[0] == 0:
        st.write("The predicted class is **Cammeo**.")
    else:
        st.write("The predicted class is **Osmancik**.")
