from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = light_spellbook.light_spell_allowed_ingredients()
    ingredients = ingredients.lower()
    if any(word in ingredients for word in valid_ingredients):
        return "VALID"
    else:
        return "INVALID"
