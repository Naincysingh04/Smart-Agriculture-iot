import joblib 
import numpy as np 

class IrrigationModel:
    def __init__(self, model_path='model.pkl'):
        self.model = joblib.load(model_path)

    def predict(self, moisture, temperature):
        features = np.array([[moisture, temperature]])
        prediction = self.model.predict(features)[0]
        return prediction  # 1 = Irrigation Needed, 0 = Not Needed
