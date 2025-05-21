import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from common.helper_functions import print_llm_response, get_llm_response

print_llm_response("Hello, world! my name is Peter")
print(get_llm_response("Tell me a good joke with 2 sentences."))
