# %% section 1
from helper_functions import upload_txt_file, list_files_in_directory, print_llm_response
import os
# script_dir = os.path.dirname(os.path.abspath(__file__))
list_files_in_directory()

# %% section 2
# Open the email.txt file and print its contents
f = open("email.txt", "r")
email = f.read()
f.close()

print(email)

# Open the recipe.txt file and print its contents
f = open("recipe.txt", "r")
recipe = f.read()
f.close()

print(recipe)

# %% section 3
upload_txt_file() 


# Change the file name on the next line to the one you uploaded. 
# Make sure you keep the double quotation marks around the file name!
f = open("jot-down.txt", "r", encoding='utf-8')
your_file_content = f.read() 
f.close()

print(your_file_content)

# %% section 4

# Modify the prompt below to ask the LLM a different question about 
# your data
prompt = f"""What is the next step for my working. you can plan the next step. 

Text:
{your_file_content}"""

print_llm_response(prompt)

# %% section 5
# Modify the prompt to use the data that you loaded in from recipe.txt
# Hint: look back throughout the notebook for the variable you stored 
# the recipe data in.
prompt = f"""Identify all of the cooking techniques used in the 
following recipe:

Recipe:
{recipe}"""

print_llm_response(prompt)