# Walmart-Trends
Dataset: https://www.kaggle.com/datasets/yasserh/walmart-dataset
1) Which product categories show highest sales volatility weekly?
2) Do holiday weeks significantly outperform regular weeks?
3)  Can we predict weekly sales using pricing and promotion data?
4)   How does temperature affect sales of seasonal products?
5)   Which 3 factors most influence store performance differences?

LightGBM Prediction App (Flask + GitHub Codespaces)

This is a simple Flask web application that uses a pre-trained LightGBM model to make predictions based on user input. It is designed to run easily inside GitHub Codespaces.

Features

- Trained LightGBM model with `scikit-learn` pipeline
- Interactive web form to collect input features
- Predict output using the model
- Lightweight Flask backend
- Ready to run in GitHub Codespaces or locally

Project Structure

project-root/

├── app.py # Main Flask application

├── lgbm_model_pipeline.joblib # Trained model pipeline (joblib)

├── templates/

│ └── index.html # HTML form for user input

├── requirements.txt # Python dependencies

1. Clone the Repository 

bash

git clone https://github.com/umair03502/Walmart-Trends.git

cd Walmart-Trends/Application

2. Create Virtual Environment
   
python -m venv venv

source venv/bin/activate

On Windows use:

venv\Scripts\activate

4. Install Dependencies
   
pip install -r requirements.txt

6. Run the Flask App
   
python app.py





