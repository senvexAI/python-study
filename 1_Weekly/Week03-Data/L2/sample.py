from helper_functions import upload_txt_file, list_files_in_directory, print_llm_response
import csv
import os

def read_csv(file):
    filepath = os.path.join(os.path.dirname(__file__), file)
    with open(filepath, "r", encoding="utf-8-sig") as f:
        csv_reader = csv.reader(f)
        rows = []
        for row in csv_reader:
            clean_row = [cell.replace('\xa0', ' ').strip() for cell in row]
            rows.append(clean_row)
    return rows
clean_data = read_csv("samp.csv")
print(clean_data)

prompt = f"""업무 진행 단계 (계획 / 진행 / 대기 / 완료 등)를 자동 분류해줘. Answer in Korean.
Text:
{clean_data}"""

print_llm_response(prompt)