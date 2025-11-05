from flask import Flask, request, jsonify
from flask_cors import CORS
from model.predict import predict_image

app = Flask(__name__)
CORS(app)

@app.route('/api/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['file']
    result = predict_image(file)
    return jsonify(result)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': '🧬 Cancer Detection API is running'})

if __name__ == '__main__':
    app.run(debug=True)
