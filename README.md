# Rice Classification Model

This repository contains a Machine Learning Model for classifying rice varieties based on various features. The model was trained using Support Vector Classification (SVC) algorithm and achieves an accuracy of 92%.

## Project Structure
 - app.py                # Streamlit application
 - model                 # Directory containing the saved models
 - grid_classifier.pkl  # Trained model
 - scaled1.pkl          # Scaler for input features
 - requirements.txt      # Required packages
 - README.md             # Project documentation


## Features

- **Input Features**: 
  - Area
  - Perimeter
  - Major Axis Length
  - Minor Axis Length
  - Eccentricity
  - Convex Area
  - Extent

- **Output**: Predicts the class of rice (e.g., Cammeo or Osmancik).

## Provided Files

- **Model Files**:
  - `grid_classifier.pkl`: This is the trained SVC model that can be used for predictions.
  - `scaled1.pkl`: This file contains the scaler used to normalize input features between 0 and 1.

- **Jupyter Notebook**:
  - `back_end.ipynb`: A comprehensive notebook that includes data cleaning, data visualization, preprocessing steps, and model training. This allows you to review the code and understand the entire process. You can also use it to retrain the model from scratch if desired.
    
## Usage

1. Clone the repository:
git clone https://github.com/Akshint0407/Rice-Classification-Model.git
cd Rice-Classification-Model

2. Install the required packages:
pip install -r requirements.txt

3. Run the Streamlit app on cmd:
streamlit run app.py

4. Input the values for the features and click the predict button to see the predicted class.

## Live Demo

You can view the deployed application at the following link:

[![Visit the Rice Classification Model][(https://img.shields.io/badge/Streamlit-App-blue)](https://rice-classification-model-r5ckfnelx9dkyaeowmbug4.streamlit.app/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
