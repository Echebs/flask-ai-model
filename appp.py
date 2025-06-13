from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import random

app = Flask(__name__)

# Load your AI model
model = tf.keras.models.load_model("FINALYEAR_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = np.array(data['input']).reshape(1, 6, 4)  # Adjust shape as needed
    prediction = model.predict(input_data)
    return jsonify({
        "predicted_power": float(prediction[0][0]),
        "anomaly_score": float(prediction[0][1])
    })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # You can replace these with real sensor readings
    voltage = round(random.uniform(210, 230), 2)
    current = round(random.uniform(4.0, 6.0), 2)
    power = round(voltage * current, 2)
    anomaly = power > 1300  # Example threshold

    return jsonify({
        "voltage": voltage,
        "current": current,
        "power": power,
        "anomaly": anomaly
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
