# %% section 1

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from common.helper_functions import print_llm_response, get_llm_response

task_list = [
    {
        "description": "Compose a brief email to my boss explaining that I will be late for next week's meeting.",
        "time_to_complete": 3
    },
    {
        "description": "Create an outline for a presentation on the benefits of remote work.",
        "time_to_complete": 60
    },
    {
        "description": "Write a 300-word review of the movie 'The Arrival'.",
        "time_to_complete": 30
    },
    {
        "description": "Create a shopping list for tofu and olive stir fry in 100-words or less.",
        "time_to_complete": 5
    }
]

task=task_list[3]

print(task)

task["time_to_complete"] <= 5

if task["time_to_complete"] <= 5:
    task_to_do = task["description"]
    print_llm_response(task_to_do)
    
# %% section 2

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do)
    else:
        print(f"To complete later: {task['time_to_complete']} time to complete")




# %% section 3
tasks_for_later = []

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do)
    else:
        tasks_for_later.append(task)

print(tasks_for_later)


# %% section 4
# Modify this code to complete the task 
# if it takes more than 15 minutes

task = task_list[2]

### EDIT THE FOLLOWING CODE ###
if task["time_to_complete"] > 15: #Modify this line
    task_to_do = task["description"]
    print_llm_response(task_to_do)
### --------------- ###

# %% section 5

# Fix the code here by only using indentation.
# It should print a message if the "Chocolate" ice cream flavor 
# is located in the ice_cream_flavors list.

ice_cream_flavors = [
    "Vanilla", "Strawberry", "Mint Chocolate Chip",
    "Cookies and Cream", "Rocky Road", "Butter Pecan",
    "Pistachio", "Salted Caramel", "Chocolate",
    "Mango"
]

### EDIT THE FOLLOWING CODE ### 
#Hint: Recall that the code within for loops 
# and if statements is indented. The convention
# in Python is to add four spaces for indented code.
for flavor in ice_cream_flavors:
    if flavor == "Chocolate":
        print(f"The list of flavors contains {flavor}, Andrew's favorite.")
### --------------- ###

# %% section 6
# Add variables to the f-string to provide the
# task description as well as the time to complete 
# for the tasks that are left for later.

for task in task_list:
    if task["time_to_complete"] <= 5:
        task_to_do = task["description"]
        print_llm_response(task_to_do) 
    else:
        ### EDIT THE FOLLOWING CODE ###
        # Hint: To add a variable in an f-string
        # you need to use the following syntax: {variable_name}. 
        print(f"To complete later: {task['description']} in ({task['time_to_complete']} minutes)") 
        ### ---------------  ###


