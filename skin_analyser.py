
class SkinAnalyser:
    def __init__(self):
        pass

    def analyse(self, skin_profile):
        # This properly extracts data from the SkinProfile object
        return {
            "age": skin_profile.age,
            "gender": getattr(skin_profile, 'gender', 'unknown'), # Handle missing gender safely
            "skin_type": skin_profile.skin_type,
            "concerns": ",".join(getattr(skin_profile, 'concerns', [])) # Handle missing concerns safely
        }
