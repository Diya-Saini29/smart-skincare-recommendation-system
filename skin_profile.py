class SkinProfile:
    def __init__(self, skin_type, oiliness, dryness, sensitivity,
                 acne, dark_spots, redness, age):

        self.skin_type = skin_type
        self.oiliness = oiliness
        self.dryness = dryness
        self.sensitivity = sensitivity
        self.acne = acne
        self.dark_spots = dark_spots
        self.redness = redness
        self.age = age

    def to_dict(self):
        return {
            "skin_type": self.skin_type,
            "oiliness_level": self.oiliness,
            "dryness_level": self.dryness,
            "sensitivity_level": self.sensitivity,
            "acne_severity": self.acne,
            "dark_spots_level": self.dark_spots,
            "redness_level": self.redness,
            "age": self.age
        }
