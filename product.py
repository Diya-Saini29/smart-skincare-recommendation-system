import json
class Product:
    def __init__(self, pid, name, skin_type, concerns, ingredients):
        self.pid = pid
        self.name = name
        self.skin_type = skin_type
        self.concerns = concerns
        self.ingredients = ingredients

class ProductDatabase:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_products(self):
        with open(self.file_path, "r") as f:
            data = json.load(f)

        products = []

        if isinstance(data, dict):
            # Dictionary: each key maps to a list of products
            for key, prod_list in data.items():
                for p in prod_list:
                    products.append(
                        Product(
                            pid=p["id"],
                            name=p["name"],
                            skin_type=p["skin_type"],
                            concerns=p["concerns"],
                            ingredients=p["ingredients"]
                        )
                    )
        elif isinstance(data, list):
            # List of products
            for p in data:
                products.append(
                    Product(
                        pid=p["id"],
                        name=p["name"],
                        skin_type=p["skin_type"],
                        concerns=p["concerns"],
                        ingredients=p["ingredients"]
                    )
                )
        else:
            raise ValueError("Unsupported JSON format for products")

        return products
