import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import my_aisetup
# Get the directory where test2.py is located
current_script_directory = os.path.dirname(os.path.abspath(__file__))
print(f"현재 스크립트 디렉토리: {current_script_directory}")
print(f"디렉토리 내 파일/폴더 목록: {os.listdir(current_script_directory)}")
my_aisetup.list_files_in_directory(current_script_directory) 

print("--------------------------------")
print(os.listdir(current_script_directory))
print(os.listdir())
print("--------------------------------")

# Print sys.path
print("--- sys.path ---")
for path in sys.path:
    print(path)
print("----------------")

# 현재 파일의 경로 출력
import os
print("--- os.path ---")
print(os.path.abspath(__file__))
print("----------------")
print("--- os.getcwd ---")
print(os.getcwd())
print("----------------")
print(os.listdir(os.getcwd()))
print("----------------")