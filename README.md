# Walmart-Trends
Dataset: https://www.kaggle.com/datasets/yasserh/walmart-dataset
1) Which product categories show highest sales volatility weekly?
2) Do holiday weeks significantly outperform regular weeks?
3)  Can we predict weekly sales using pricing and promotion data?
4)   How does temperature affect sales of seasonal products?
5)   Which 3 factors most influence store performance differences?

Answers with plots:
1) ![image](https://github.com/user-attachments/assets/9a12b5c7-068b-4e41-b429-a8de32afe7ef)

Weekly sales vary widely across stores.
Some stores show high sales with large fluctuations.
Several stores have extreme outlier sales weeks.
Low-sales stores tend to have more stable sales.
Sales volatility suggests different store management needs.

2) ![image](https://github.com/user-attachments/assets/2962d340-e1a6-49cf-a61e-142f4818acf4)

The data confirms that on average, holiday weeks outperform regular weeks in sales.
The presence of error bars helps to visualize uncertainty and is good practice to assess reliability.
Further statistical testing could validate if the difference is statistically significant.

3)![image](https://github.com/user-attachments/assets/f0c6252b-fa19-4207-801d-182ba772487c)

The sales distribution during holiday weeks is clearly different and often higher compared to non-holiday weeks.
This suggests that holiday weeks significantly outperform regular weeks in terms of weekly sales, with more sales volume and more variability.
The multiple peaks in the holiday sales density may reflect different types or intensities of holiday promotions or shopping spikes.

4)![image](https://github.com/user-attachments/assets/6d954d35-facc-4b53-af73-3ef646bd60bf)

Weekly sales do not show a strong direct correlation with temperature; sales are spread broadly across all temperature ranges.
Holiday weeks (orange points) appear more scattered and less dense compared to non-holiday weeks (blue points), indicating fewer observations during holidays.
There is no clear pattern suggesting that temperature significantly influences sales during holiday or non-holiday weeks.
Sales peak values (close to 3.5-4 million) appear in both low and moderate temperature ranges but are rare overall.
The plot suggests other factors beyond temperature likely play a larger role in driving weekly sales.


5)Top 3 factors influencing store performance:
 Unemployment   -0.112281
 CPI            -0.076569
 Temperature    -0.076388
 Name: Weekly_Sales, dtype: float64
 
i) Unemployment (-0.112) has the strongest negative impact on Weekly Sales among the three factors — as unemployment rises, weekly sales tend to decrease slightly.
ii) CPI (-0.077) (Consumer Price Index) also negatively correlates with sales, implying that higher inflation or prices correspond to a small drop in weekly sales.
iii) Temperature (-0.076) shows a mild negative relationship with sales — higher temperatures are slightly associated with lower sales.




LightGBM Prediction App (Flask + GitHub Codespaces)

This is a simple Flask web application that uses a pre-trained LightGBM model to make predictions based on user input.

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

```bash

git clone https://github.com/umair03502/Walmart-Trends.git

```bash

cd Walmart-Trends/Application

2. Create Virtual Environment

```bash
   
python -m venv venv

On Linux use:

```bash
source venv/bin/activate

On Windows use:

```bash
venv\Scripts\activate

4. Install Dependencies

```bash
pip install -r requirements.txt

6. Run the Flask App

```bash
python app.py





