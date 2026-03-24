import json
import os

class RecommendationEngine:
    def __init__(self, product_file="data/product.json"):
        self.products = {}
        self.fallback_map = {
            "pigmentation": ["balanced", "sensitive"], 
            "prone": ["balanced"]
        }
        
        if os.path.exists(product_file):
            try:
                with open(product_file, "r", encoding="utf-8") as f:
                    self.products = json.load(f)
            except:
                print("[ERROR] Invalid JSON in product.json")
        else:
            print(f"[ERROR] Missing {product_file}")

    def recommend(self, predicted_label: str):
        search_term = predicted_label.lower().strip()
        recommendations = []
        
        keywords = search_term.replace("&", " ").replace("-", " ").split()
        
        found_keys = []
        for word in keywords:
            for key in self.products.keys():
                if word in key or key in word:
                    if key not in found_keys:
                        recommendations.extend(self.products[key])
                        found_keys.append(key)
            if word in self.fallback_map:
                for fallback_key in self.fallback_map[word]:
                    if fallback_key in self.products and fallback_key not in found_keys:
                        recommendations.extend(self.products[fallback_key])
                        found_keys.append(fallback_key)

        seen_names = set()
        unique_recs = []
        for p in recommendations:
            if p.get("name") not in seen_names:
                unique_recs.append(p)
                seen_names.add(p.get("name"))

        if not unique_recs:
            return self.products.get("balanced", [])

        return unique_recs
