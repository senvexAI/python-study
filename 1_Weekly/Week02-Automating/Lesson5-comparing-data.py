import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from common.helper_functions import print_llm_response, get_llm_response

food_preferences_tommy = {
    #"dietary_restrictions": "vegetarian",
    "favorite_ingredients": ["mushrooms", "olives"],
    "experience_level": "intermediate",
    "maximum_spice_level": 6
}

food_preferences_tommy["is_vegetarian"] = True

print(food_preferences_tommy)