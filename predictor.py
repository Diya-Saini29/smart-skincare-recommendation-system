
import pandas as pd
import numpy as np
from backend.model_loader import ModelLoader

class Predictor:
    def __init__(self):
        loader = ModelLoader()
        self.pipeline = loader.get_model()
        self.encoder = loader.get_label_encoder() 

    def predict(self, profile_data: dict):
        try:
           
            mappings = {
                "oiliness": "oiliness_level",
                "dryness": "dryness_level",
                "sensitivity": "sensitivity_level",
                "acne": "acne_severity",
                "dark_spots": "dark_spots_level",
                "redness": "redness_level"
            }
            
            cleaned_data = {}
            for k, v in profile_data.items():
                new_key = mappings.get(k, k)
                cleaned_data[new_key] = v

            df = pd.DataFrame([cleaned_data])

         
            numeric_cols = ["oiliness_level", "dryness_level", "sensitivity_level", 
                            "acne_severity", "dark_spots_level", "redness_level", "age"]
            
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
                else:
                    df[col] = 0

            if "skin_type" in df.columns:
                df["skin_type"] = df["skin_type"].astype(str).str.lower()


            final_label = self.pipeline.predict(df)[0]

            return final_label.lower().replace("skin", "").strip()

        except Exception as e:
            print(f"\n[ERROR in Predictor] {str(e)}")
            import traceback
            traceback.print_exc()
            return "balanced"