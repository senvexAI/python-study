from helper_function import print_llm_response, get_llm_response, display_table
from IPython.display import Markdown
import csv
import os

def read_csv(file):
    f = open(file, "r")
    
    csv_reader = csv.DictReader(f)
    data = []
    for row in csv_reader:
        data.append(row)
    f.close()
    
    return data

# Read the itinerary.csv file
itinerary = read_csv(os.path.join(os.path.dirname(__file__), "itinerary.csv"))


# Display the itinerary
display_table(itinerary)