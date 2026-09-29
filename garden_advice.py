def get_season_advice(season):
    """
    Return gardening advice based on the season.
    
    Args:
        season (str): The current season (e.g., 'summer', 'winter').
        
    Returns:
        str: Advice for the given season.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"

def get_plant_advice(plant_type):
    """
    Return gardening advice based on the plant type.
    
    Args:
        plant_type (str): The type of plant (e.g., 'flower', 'vegetable').
        
    Returns:
        str: Advice for the given plant type.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."

def generate_advice(season, plant_type):
    """
    Combine season and plant advice into a single message.
    
    Args:
        season (str): The current season.
        plant_type (str): The type of plant.
        
    Returns:
        str: Combined gardening advice.
    """
    return get_season_advice(season) + get_plant_advice(plant_type)

# Main program
if __name__ == "__main__":
    # Ask the user for input
    season = input("Enter the season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()
    
    # Generate and print the advice
    advice = generate_advice(season, plant_type)
    print(advice)