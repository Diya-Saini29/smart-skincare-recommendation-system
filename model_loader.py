import pickle

class ModelLoader:
    def __init__(self, model_path="ml/model.pkl", encoder_path="ml/label_encoder.pkl"):
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        with open(encoder_path, "rb") as f:
            self.label_encoder = pickle.load(f)

    def get_model(self):
        return self.model

    def get_label_encoder(self):
        return self.label_encoder
