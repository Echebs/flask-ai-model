from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load your model
model = tf.keras.models.load_model('FINALYEAR_model.h5', compile=False)


@app.route('/')
def home():
    return "Your AI Model is Live"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # expects: {"input": [list of numbers]}
    input_array = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_array)
    return jsonify({'prediction': prediction.tolist()})
if __name__ == "__main__":
    app.run(debug=True)
