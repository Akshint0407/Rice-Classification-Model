# Rice Classification Model

This repository contains a Machine Learning Model for classifying rice varieties based on various features. The model was trained using Support Vector Classification (SVC) algorithm and achieves an accuracy of 92%.

## Project Structure
 *rice-classification-model*
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

- **Output**: Predicts the class of rice (e.g., Cammeo).

## Usage

1. Clone the repository:
git clone https://github.com/Akshint0407/Rice-Classification-Model.git
cd Rice-Classification-Model


2. Install the required packages:
pip install -r requirements.txt

3. Run the Streamlit app on cmd:
streamlit run app.py


4. Input the values for the features and click the predict button to see the predicted class.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
