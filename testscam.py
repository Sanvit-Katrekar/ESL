from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain import hub
import warnings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import AzureChatOpenAI
from langchain.docstore.document import Document
import textwrap

from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_TYPE"] = os.getenv('API_TYPE')
os.environ["OPENAI_API_KEY"] = os.getenv('OPEN_AI_KEY')
os.environ["OPENAI_API_BASE"] = os.getenv('ENDPOINT')
os.environ["OPENAI_API_VERSION"] = os.getenv('API_VERSION')
model = AzureChatOpenAI(deployment_name=os.getenv('ENGINE'), temperature=0.7)

warnings.filterwarnings('ignore')

def get_prediction(question: str) -> list[dict]:
    PROMPT = """
    [INST]
    <<SYS>>
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

    <<SYS>>
    Sentence to translate: {question}
    Answer: 
    [/INST]"""

    loader = TextLoader("data/en-data.txt")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

    #question = "I love to swim in the swimming pool after painting"
    #question = 'I love to paint before swimming'
    #question = 'I love to play football at the sports union before painting'
    #question = 'The knife is playing basketball'
    docs = vectorstore.similarity_search(question)

    rag_prompt_llama = hub.pull("rlm/rag-prompt-llama")
    rag_prompt_llama.messages[0].prompt.template = PROMPT

    chain = load_qa_chain(model, chain_type="stuff", prompt=rag_prompt_llama)

    result = chain({"input_documents": docs, "question": question}, return_only_outputs=True)

    print('\n\n')

    output_str: str = result['output_text']
    print(output_str)
    try:
        start_index = output_str.index('{')
        end_index = output_str.index(']') + 1
        output = eval('[' + output_str[start_index: end_index])
    except:
        start_index = output_str.index('{')
        end_index = output_str.index('}') + 1
        output = [eval(output_str[start_index: end_index])]

    return output

if __name__ == '__main__':
    # prediction = "The Lion is swimming in the swimming pool while The oven is baking a cake."
    prediction = "Hello, I am Bhavya"
    output = get_prediction(prediction)
    print(output)