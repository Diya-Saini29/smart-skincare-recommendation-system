'''from flask import Flask, render_template, request
from backend.skin_profile import SkinProfile
from backend.predictor import Predictor
from backend.reccomender import RecommendationEngine

app = Flask(__name__, static_folder="ui", template_folder="ui")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    SKIN_TYPE_MAP = {
        "0": "dry",
        "1": "oily",
        "2": "sensitive",
        "3": "balanced"
    }

    skin_type_input = request.form.get("skin_type", "3")  
    skin_type = SKIN_TYPE_MAP.get(skin_type_input, "balanced")

    try:
        oiliness = int(request.form.get("oiliness", 0))
        dryness = int(request.form.get("dryness", 0))
        sensitivity = int(request.form.get("sensitivity", 0))
        acne = int(request.form.get("acne", 0))
        dark_spots = int(request.form.get("dark_spots", 0))
        redness = int(request.form.get("redness", 0))
        age = int(request.form.get("age", 25))
    except:
        oiliness = dryness = sensitivity = acne = dark_spots = redness = 0
        age = 25

    profile = SkinProfile(
        skin_type=skin_type,
        oiliness=oiliness,
        dryness=dryness,
        sensitivity=sensitivity,
        acne=acne,
        dark_spots=dark_spots,
        redness=redness,
        age=age
    )

    predictor = Predictor()
    predicted_label = predictor.predict(profile.to_dict())

    recommender = RecommendationEngine()
    products = recommender.recommend(predicted_label)

    return render_template(
        "result.html",
        label=predicted_label,
        products=products
    )

if __name__ == "__main__":
    app.run(debug=True)
'''
from flask import Flask, render_template, request
from backend.skin_profile import SkinProfile
from backend.predictor import Predictor
from backend.reccomender import RecommendationEngine # Ensure filename is recommender.py

app = Flask(__name__, static_folder="ui", template_folder="ui")

# Initialize Models ONCE (Global Scope) for performance
predictor = Predictor()
recommender = RecommendationEngine()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    # Map form values "0" -> "dry" to match training data
    SKIN_TYPE_MAP = {"0": "dry", "1": "oily", "2": "sensitive", "3": "balanced"}
    
    skin_type_input = request.form.get("skin_type", "3")  
    skin_type = SKIN_TYPE_MAP.get(skin_type_input, "balanced")

    # Safe Integer Conversion
    try:
        profile = SkinProfile(
            skin_type=skin_type,
            oiliness=int(request.form.get("oiliness", 0)),
            dryness=int(request.form.get("dryness", 0)),
            sensitivity=int(request.form.get("sensitivity", 0)),
            acne=int(request.form.get("acne", 0)),
            dark_spots=int(request.form.get("dark_spots", 0)),
            redness=int(request.form.get("redness", 0)),
            age=int(request.form.get("age", 25))
        )
    except ValueError:
        return "Invalid Input", 400

    # Predict & Recommend
    predicted_label = predictor.predict(profile.to_dict())
    products = recommender.recommend(predicted_label)

    return render_template(
        "result.html",
        label=predicted_label,
        products=products
    )

if __name__ == "__main__":
    app.run(debug=True)