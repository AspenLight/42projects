from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = dark_spell_allowed_ingredients()
    ingredients = ingredients.lower()
    if any(word in ingredients for word in valid_ingredients):
        return "VALID"
    else:
        return "INVALID"
