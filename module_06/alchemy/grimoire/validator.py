def validate_ingredients(ingredients: str) -> str:
    for word in ingredients.split():
        if word not in ["fire", "water", "earth", "air"]:
            return f"{ingredients} - INVALID"
    else:
        return f"{ingredients} - VALID"
