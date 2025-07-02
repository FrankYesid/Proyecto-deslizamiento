import numpy as np
from PIL import Image
from typing import Dict, Any
import mlflow
import mlflow.pyfunc
from app.config.settings import settings

class MLInferenceService:
    def __init__(self):
        """
        Initializes the MLInferenceService.
        Sets the MLflow tracking URI and loads the default model.
        """
        self.models = {}
        mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
        self.load_model(settings.DEFAULT_MODEL)

    def load_model(self, model_name: str, model_stage: str = "Production"):
        """
        Load an ML model from the MLflow Model Registry.
        The model is loaded as a pyfunc model.
        """
        model_uri = f"models:/{model_name}/{model_stage}"
        try:
            self.models[model_name] = mlflow.pyfunc.load_model(model_uri)
            print(f"Successfully loaded model '{model_name}' from stage '{model_stage}'.")
        except Exception as e:
            print(f"Error loading model '{model_name}' from stage '{model_stage}': {e}")
            self.models[model_name] = None

    def preprocess_image(self, image: Image.Image) -> np.ndarray:
        """
        Preprocess image for model input.
        This is a placeholder and should be adapted to your model's requirements.
        """
        # Example preprocessing: resize and convert to numpy array
        image = image.resize((224, 224))
        return np.array(image)

    def classify_image(self, image: Image.Image, model_name: str) -> Dict[str, Any]:
        """
        Classify a satellite image using a model from the MLflow Model Registry.
        """
        if model_name not in self.models or self.models[model_name] is None:
            self.load_model(model_name)
            if self.models.get(model_name) is None:
                 return {
                    "error": f"Model '{model_name}' could not be loaded."
                }

        processed_image = self.preprocess_image(image)
        
        import pandas as pd
        model_input = pd.DataFrame([processed_image.flatten()])

        model = self.models[model_name]
        try:
            prediction = model.predict(model_input)
            
            if isinstance(prediction, np.ndarray):
                result = {
                    "classification": str(prediction.argmax()),
                    "confidence": float(prediction.max())
                }
            else:
                result = {"prediction": str(prediction)}

            return result

        except Exception as e:
            print(f"Error during inference with model '{model_name}': {e}")
            return {
                "error": f"An error occurred during inference with model '{model_name}'."
            }
