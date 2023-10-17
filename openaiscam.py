import openai
import os
from dotenv import load_dotenv

load_dotenv()
with open('data/en-data.txt') as f:
    context = f.read()
class OpenAIClient:
    def __init__(self):
        self.api_key = os.getenv('OPEN_AI_KEY')
        self.endpoint = os.getenv('ENDPOINT')
        self.api_version = os.getenv('API_VERSION')
        self.api_type = os.getenv('API_TYPE')
        self.engine=os.getenv('ENGINE')
        self.chat=openai.ChatCompletion
        self.__init_openai__()
    
    def __init_openai__(self):
        openai.api_type = self.api_type
        openai.api_base = self.endpoint
        openai.api_version = self.api_version
        openai.api_key = self.api_key
        openai.engine=self.engine

    def generate_mappings(self, content):
        response = self.chat.create(
            engine='techbuzzrss',
            temperature=0.6,
            messages=[
                {
                    "role": "system",
                    "content": f"""
                    You are a sign language translator assistant.
    You will be given context of phrases mapped to a video link, of the format:

    "First Phrase: First phrase video link" i.e., the context contains phrase and link delimited by a ':'

    Your vocabulary is strictly restricted to the phrases provided in:

    {context}

    The above phrases are also presented in the document, used for question answering.

    Strictly follow the 7 rules provided below::
    1. Assistant translates for a language restricted to the vocabulary provided above.
    2. Assistant translates for a language without prepositions and grammatical phrases.
    3. Make meaningful translations.
    4. Replace phrases in the sentence with their synonyms or closest matches from the provided vocabulary.
    5. No prepositions or grammatical phrases in the translation, the sentence is simplified to just the main phrases.
    6. In case the phrase does not exist in the vocabulary, replace with individual letters.
    7. Omit all unnecessary words/phrases not having any effect on the semantic meaning of the sentence.
    8. Links provided for the phrases should be valid links taken directly from the context provided.

    Just return the final output in the following format, assuming there are 'n' phrases:
    [{{
        "phrase": "Closest matching phrase for phrase 1 provided in context accuratelt",
        "link": "Exact link for phrase 1 provided in context accurately"
    }},
    {{
        "phrase": "Closest matching phrase for phrase 2",
        "link": "Exact link for phrase 2 provided in context"
    }},
    ...,
    {{
        "phrase": "Closest matching phrase for phrase n",
        "link": "Exact link for the phrase n context"
    }}
    ]

    wherein phrase 1, second phrase 2, phrase 3, ..., phrase n, are all phrases present in the vocabulary provided to assistant.

    Phrase should match exactly that of the phrase in the vocabulary provided as context.

    Strictly use the format above and keep the answer concise.

    Try splitting the sentence to achieve maximum number of phrases.
                    """
                },
                {
                    "role": "user",
                    "content": content
                }
            ]
        )

oai=OpenAIClient()
mappings=oai.generate_mappings("Hello I am a teacher in a school.")
print(mappings)
