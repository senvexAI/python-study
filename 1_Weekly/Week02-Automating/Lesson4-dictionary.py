import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from common.helper_functions import print_llm_response, get_llm_response


food_preferences_tommy = {
        "dietary_restrictions": "vegetarian",
        "favorite_ingredients": ["tofu", "olives"],
        "experience_level": "intermediate",
        "maximum_spice_level": 6
}
print(food_preferences_tommy.keys())


prompt = f"""Please suggest a recipe that tries to include 
the following ingredients: 
{food_preferences_tommy["favorite_ingredients"]}.
The recipe should adhere to the following dietary restrictions:
{food_preferences_tommy["dietary_restrictions"]}.
The difficulty of the recipe should be: 
{food_preferences_tommy["experience_level"]}
The maximum spice level on a scale of 10 should be: 
{food_preferences_tommy["maximum_spice_level"]} 
Provide a two sentence description.
"""

print(prompt)
# print_llm_response(prompt)

available_spices = ["cumin", "turmeric", "paprika"]


prompt = f"""Please suggest a recipe that tries to include 
the following ingredients: 
{food_preferences_tommy["favorite_ingredients"]}.
The recipe should adhere to the following dietary restrictions:
{food_preferences_tommy["dietary_restrictions"]}.
The difficulty of the recipe should be: 
{food_preferences_tommy["experience_level"]}
The maximum spice level on a scale of 10 should be: 
{food_preferences_tommy["maximum_spice_level"]} 
Provide a two sentence description.

The recipe should not include spices outside of this list:
Spices: {available_spices}
"""
print(prompt)

# recipe = get_llm_response(prompt)
# print(recipe)




# Update the following dictionary 
# with your own preferences 

### EDIT THE FOLLOWING CODE ###
my_food_preferences = {
        "dietary_restrictions": ["non-vegetarian"], #List with dietary restrictions
        "favorite_ingredients": ["duck", "pork", "chicken"], #List with top three favorite ingredients
        "experience_level": "intermediate", #Experience level
        "maximum_spice_level": 8 #Spice level in a scale from 1 to 10
}
### --------------- ###

print(my_food_preferences)


# Modify the following prompt, 
# without adding more than two sentences,
# so that the provided recipe includes detailed instructions.

### EDIT THE FOLLOWING CODE ###
#Hint: look at the last sentence in this prompt
prompt = f"""Please suggest a recipe that tries to include 
the following ingredients: 
{my_food_preferences["favorite_ingredients"]}.
The recipe should adhere to the following dietary restrictions:
{my_food_preferences["dietary_restrictions"]}.
The difficulty of the recipe should be: 
{my_food_preferences["experience_level"]}
The maximum spice level on a scale of 10 should be: 
{my_food_preferences["maximum_spice_level"]} 
Provide a two sentence description only.
"""
### --------------- ###

print_llm_response(prompt)