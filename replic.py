'''
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

os.environ["REPLICATE_API_TOKEN"] = os.getenv('REPLICATE_API_TOKEN')

from langchain.llms import Replicate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Replicate(
    model="meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    model_kwargs={"temperature": 0.75, "max_length": 500, "top_p": 1},
)
prompt = """
User: Convert the sentence "hello there!" in arabic
Assistant:
"""
print(llm(prompt))


'''
import replicate

with open('vocabulary.txt') as f:
    content = f.read()
output = replicate.run(
    "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    input={"system_prompt": f"""
You are a translator assistant.
Vocabulary strictly restricted to :
{content}
Make sure that:
1. Restricted to the vocabulary provided above.
2. Assistant translates for a language without prepositions and grammatical words.
3. Make meaningful translations.
4. Closest words and synonyms
5. In case doesnt not exist replace with individual letters.
Return ouput in the format:
["first word", "second word", "third word", ...., "last word"]
where in first word, second word, third word are all words present in the vocabulary provided to assistant.
Strictly use the format above.
Make sure
Sentence to translate: ""","prompt" : "The man is swimming by the pool far away."
}
)
# The meta/llama-2-70b-chat model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/meta/llama-2-70b-chat/versions/02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3/api#output-schema
    print(item, end="")



