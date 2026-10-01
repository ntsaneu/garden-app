# Garden Advice App
# TODO / CHANGE LOG
# 2024-05-24: Replaced hardcoded values with input() (Issue #1)
# 2024-05-24: Refactored code into functions and added docstrings (Issue #2)
# 2024-05-24: Refactored advice storage to use dictionaries (Issue #3)
# 2024-05-24: Added plant suggestions based on season (Issue #4)

# Dictionary mappings for advice and suggestions
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n"
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}

PLANT_SUGGESTIONS = {
    "summer": "Sunflowers, Tomatoes, and Zinnias thrive in summer.",
    "winter": "Pansies, Kale, and Winter Jasmine thrive in winter."
}

def get_season_advice(season):
    """Return gardening advice based on the season."""
    return SEASON_ADVICE.get(season, "No advice for this season.\n")

def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")

def get_plant_suggestions(season):
    """Return plant suggestions based on the season."""
    return PLANT_SUGGESTIONS.get(season, "No plant suggestions available.")

def generate_advice(season, plant_type):
    """Combine season, plant advice, and suggestions into a single message."""
    advice = get_season_advice(season) + get_plant_advice(plant_type)
    advice += f"\n\nSuggested plants for {season}: {get_plant_suggestions(season)}"
    return advice

# Main program
if __name__ == "__main__":
    season = input("Enter the season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()
    
    advice = generate_advice(season, plant_type)
    print(advice)