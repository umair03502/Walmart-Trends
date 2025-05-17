from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('lgbm_model_pipeline.joblib')  # Load trained model

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        try:
            store = int(request.form['store'])
            holiday_flag = int(request.form['holiday_flag'])
            temperature = float(request.form['temperature'])
            fuel_price = float(request.form['fuel_price'])
            cpi = float(request.form['cpi'])
            unemployment = float(request.form['unemployment'])

            features = np.array([[store, holiday_flag, temperature, fuel_price, cpi, unemployment]])
            prediction = model.predict(features)[0]
            prediction = f"${prediction:,.2f}"  # Format as currency
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
