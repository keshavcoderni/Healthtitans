from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained AI model
model = joblib.load("maternal_health_model.pkl")

@app.route('/')
def home():
    return "Healthcare AI API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get data from frontend
        df = pd.DataFrame([data])  # Convert to DataFrame

        # Select only relevant columns
        features = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]
        df = df[features]

        # Make prediction
        prediction = model.predict(df)[0]

        # Map numeric prediction back to labels
        risk_levels = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
        result = risk_levels[prediction]

        return jsonify({"Risk Level": result})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
