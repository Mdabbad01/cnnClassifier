from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.prediction import PredictionPipeline

# Set environment encoding
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Client app to hold classifier instance
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        try:
            self.classifier = PredictionPipeline(self.filename)
        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            self.classifier = None

# Home route - renders modern UI
@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

# Training route
@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    try:
        os.system("python main.py")
        # os.system("dvc repro")  # Uncomment if using DVC
        return jsonify({"status": "Training done successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Predict route
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        # Check if classifier is loaded
        if not clApp.classifier:
            return jsonify({"error": "Model not loaded. Please train or check model path."}), 500

        # Get base64 image from request
        image_base64 = request.json.get('image')
        if not image_base64:
            return jsonify({"error": "No image provided"}), 400

        # Decode image to file
        decodeImage(image_base64, clApp.filename)

        # Get prediction
        result = clApp.classifier.predict()
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True)  # debug=True helps during development
