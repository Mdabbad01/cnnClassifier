
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        """
        Initialize the prediction pipeline.
        - filename: path to the input image
        - model_path: automatically detected inside artifacts/training/model.h5
        """
        self.filename = filename

        # Calculate absolute path to project root
        # __file__ = src/cnnClassifier/pipeline/prediction.py
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        
        # Full path to the model
        self.model_path = os.path.join(project_root, "artifacts", "training", "model.h5")

        # Check if model exists
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")

        # Load model once
        self.model = load_model(self.model_path)

    def predict(self):
        """
        Predicts the class of the image.
        Returns:
            dict: {"prediction": "Tumor"} or {"prediction": "Normal"} 
                  or {"error": "error message"}
        """
        try:
            # Load image and preprocess
            test_image = image.load_img(self.filename, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)

            # Model prediction
            result = np.argmax(self.model.predict(test_image), axis=1)
            
            # Map result to label
            prediction = "Tumor" if result[0] == 1 else "Normal"

            return {"prediction": prediction}

        except Exception as e:
            # Catch any error and return JSON-friendly error message
            return {"error": str(e)}
