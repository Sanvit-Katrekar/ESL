'''
import replicate
import os
from dotenv import load_dotenv, find_dotenv
from langchain.llms import L

load_dotenv(find_dotenv())

os.environ['REPLICATE_API_TOKEN'] = os.getenv('REPLICATE_API_TOKEN')

with open('data/vocabulary.txt') as f:
    vocab = f.read()


VOCAB_PROMPT = f"""
f"This is the only vocabulary you know:
{vocab}
Answer all queries from now on in the following format:
["first word", "second_word", "third_word"]

Convert the sentence below in the format mentioned above:
I am Swimming.
"""
output = replicate.run(
    "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
    input={"prompt": VOCAB_PROMPT}
)

for item in output:
    print(item, end='')

'''

import langchain
from langchain.llms import LlamaCpp