# Dictionary mappings for advice
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n"
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!"
}

def get_season_advice(season):
    """Return gardening advice based on the season."""
    return SEASON_ADVICE.get(season, "No advice for this season.\n")

def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    return PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")

def generate_advice(season, plant_type):
    """Combine season and plant advice into a single message."""
    return get_season_advice(season) + get_plant_advice(plant_type)

# Main program
if __name__ == "__main__":
    season = input("Enter the season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()
    
    advice = generate_advice(season, plant_type)
    print(advice)