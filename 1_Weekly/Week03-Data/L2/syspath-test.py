import sys
print("--- sys.path ---")
for path in sys.path:
	print(path)
print("----------------")

import os
print("--- os.path ---")
print(os.path.abspath(__file__))
print("----------------")