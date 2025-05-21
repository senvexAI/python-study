import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from common.helper_functions import print_llm_response, get_llm_response

# ice_cream_flavors = [
#     "Vanilla: Classic and creamy with a rich, smooth flavor from real vanilla beans.",
#     "Chocolate: Deep and indulgent, made with rich cocoa for a satisfying chocolate experience.",
#     "Strawberry: Sweet and fruity, bursting with the fresh taste of ripe strawberries.",
#     "Mint Chocolate Chip: Refreshing mint ice cream studded with decadent chocolate chips.",
#     "Cookie Dough: Vanilla ice cream loaded with chunks of chocolate chip cookie dough.",
#     "Salted Caramel: Sweet and salty with a smooth caramel swirl and a hint of sea salt.",
#     "Pistachio: Nutty and creamy, featuring the distinct taste of real pistachios.",
#     "Cookies and Cream: Vanilla ice cream packed with chunks of chocolate sandwich cookies.",
#     "Mango: Tropical and tangy, made with juicy mangoes for a refreshing treat.",
#     "Rocky Road: Chocolate ice cream mixed with marshmallows, nuts, and chocolate chunks."
# ]

# print(ice_cream_flavors[2])


ice_cream_flavors = {
    "Mint Chocolate Chip": "Refreshing mint ice cream studded with decadent chocolate chips.",
    "Cookie Dough": "Vanilla ice cream loaded with chunks of chocolate chip cookie dough.",
    "Salted Caramel": "Sweet and salty with a smooth caramel swirl and a hint of sea salt."
}   

# print(ice_cream_flavors)
print(ice_cream_flavors.keys())
# print(ice_cream_flavors.values())

ice_cream_flavors["Vanilla"] = "Classic and creamy with a rich, smooth flavor from real vanilla beans."
print(ice_cream_flavors.keys())


#task example, large list not ordered by priority. Want to prioritize
list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'The Arrival'.",
    "Draft a thank-you note for my neighbor Dapinder who helped water my plants while I was on vacation.",
    "Create an outline for a presentation on the benefits of remote work."
]

#instead of that unorganized large list, divide tasks by priority
high_priority_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Create an outline for a presentation on the benefits of remote work."
]

medium_priority_tasks = [
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Draft a thank-you note for my neighbor Dapinder who helped water my plants while I was on vacation."
]

low_priority_tasks = [
    "Write a 300-word review of the movie 'The Arrival'."
]

#create dictionary with all tasks
#dictionaries can contain lists!
prioritized_tasks = {
    "high_priority": high_priority_tasks,
    "medium_priority": medium_priority_tasks,
    "low_priority": low_priority_tasks
}

print(prioritized_tasks["high_priority"])

#complete low priority tasks 
for task in prioritized_tasks["low_priority"]:
    print_llm_response(task)

