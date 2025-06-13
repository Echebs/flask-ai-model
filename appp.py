from flask import Flask
app = Flask(__name__)

from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

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
    if __name__ == "__main__":
    app.run()
