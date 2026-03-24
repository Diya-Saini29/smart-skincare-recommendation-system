import pandas as pd
import numpy as np

np.random.seed(42)

def generate_class_samples(label, n):
    if label == "Balanced":
        return pd.DataFrame({
            "skin_type": np.random.choice(["dry","oily","sensitive","balanced"], n),
            "oiliness_level": np.random.randint(3,7,n),
            "dryness_level": np.random.randint(3,7,n),
            "sensitivity_level": np.random.randint(3,7,n),
            "acne_severity": np.random.randint(0,4,n),
            "dark_spots_level": np.random.randint(0,5,n),
            "redness_level": np.random.randint(0,5,n),
            "age": np.random.randint(16,51,n),
            "label": [label]*n
        })
    elif label == "Acne-Prone":
        return pd.DataFrame({
            "skin_type": np.random.choice(["oily","acne"], n),
            "oiliness_level": np.random.randint(7,11,n),
            "dryness_level": np.random.randint(0,4,n),
            "sensitivity_level": np.random.randint(0,5,n),
            "acne_severity": np.random.randint(7,11,n),
            "dark_spots_level": np.random.randint(0,5,n),
            "redness_level": np.random.randint(3,8,n),
            "age": np.random.randint(16,51,n),
            "label": [label]*n
        })
    elif label == "Dry & Sensitive":
        return pd.DataFrame({
            "skin_type": np.random.choice(["dry","sensitive"], n),
            "oiliness_level": np.random.randint(0,4,n),
            "dryness_level": np.random.randint(7,11,n),
            "sensitivity_level": np.random.randint(7,11,n),
            "acne_severity": np.random.randint(0,5,n),
            "dark_spots_level": np.random.randint(0,6,n),
            "redness_level": np.random.randint(3,8,n),
            "age": np.random.randint(16,51,n),
            "label": [label]*n
        })
    elif label == "Oily & Acne":
        return pd.DataFrame({
            "skin_type": np.random.choice(["oily","acne"], n),
            "oiliness_level": np.random.randint(7,11,n),
            "dryness_level": np.random.randint(0,4,n),
            "sensitivity_level": np.random.randint(0,5,n),
            "acne_severity": np.random.randint(6,11,n),
            "dark_spots_level": np.random.randint(0,5,n),
            "redness_level": np.random.randint(3,7,n),
            "age": np.random.randint(16,51,n),
            "label": [label]*n
        })
    elif label == "Pigmentation-Prone":
        return pd.DataFrame({
            "skin_type": np.random.choice(["dry","balanced"], n),
            "oiliness_level": np.random.randint(2,6,n),
            "dryness_level": np.random.randint(3,7,n),
            "sensitivity_level": np.random.randint(3,7,n),
            "acne_severity": np.random.randint(0,4,n),
            "dark_spots_level": np.random.randint(7,11,n),
            "redness_level": np.random.randint(2,6,n),
            "age": np.random.randint(16,51,n),
            "label": [label]*n
        })

# Generate dataset
dfs = [generate_class_samples(lbl, 300) for lbl in ["Balanced","Pigmentation-Prone","Acne-Prone","Dry & Sensitive","Oily & Acne"]]
df = pd.concat(dfs, ignore_index=True)

# Shuffle
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save CSV
df.to_csv("data/skin_data.csv", index=False)
print("Synthetic CSV with string skin_type generated → data/skin_data.csv")
print(df['label'].value_counts())
