from langchain.chat_models import ChatOllama
from langchain.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from constants import VIDEO_DATA_PATH
from .get_arabic import get_arabic
import warnings
import json
import csv

#VIDEO_DATA_PATH = 'data/videos'

warnings.filterwarnings('ignore')

def get_prediction(question: str) -> list[dict]:
    print("Started the prediction process!")
    TEMPLATE = """
    [INST]
    <<SYS>>
    
    You are a sign language translator assistant.
    You will be given context of a CSV file, where in 'phrase' and 'video path to the respective phrase' are attributes.

    Your vocabulary is STRICTLY RESTRICTDED to the phrases provided, use the following pieces of context to translate the question at the end. 

    Here is the csv context:

    {context}

    ** IMPORTANT ** don't try to make up an answer, only answer according to the csv context provided.
    <</SYS>>

    <<SYS>>

    Strictly follow the 8 rules provided below::
    1. Assistant translates for a language restricted to the vocabulary provided above.
    2. Assistant translates for a language without prepositions and grammatical phrases.
    3. Make meaningful translations.
    4. Replace phrases in the sentence with their synonyms or closest matches from the provided vocabulary.
    5. No prepositions or grammatical phrases in the translation, the sentence is simplified to just the main phrases.
    6. **IMPORTANT** In case the phrase does not exist in the vocabulary, replace with individual letters.
    7. Omit all unnecessary words/phrases not having any effect on the semantic meaning of the sentence.
    8. Paths provided for the phrases should be valid paths taken directly from the context provided.
    9. Only use 'valid' phrases. Phrases are considered 'valid' if and only if the phrase exists in the context provided.

    <</SYS>>

    <<SYS>>

    Just return the final output in the following format, assuming there are 'n' phrases: (Note the '[')
    [
        {{
            "phrase": "Closest matching phrase for phrase 1 provided in csv context",
            "path": "Path for phrase 1 provided in csv context"
        }},
        {{
            "phrase": "Closest matching phrase for phrase 2 provided in csv context",
            "path": "Path for phrase 2 provided in csv context"
        }},
        ...,
        {{
            "phrase": "Closest matching phrase for phrase n provided in csv context",
            "path": "Path for phrase n provided in csv context"
        }}
    ]

    wherein phrase 1, second phrase 2, phrase 3, ..., phrase n, are all phrases present in the vocabulary provided to assistant.

    Phrase should match exactly that of the phrase in the vocabulary provided as context.

    Strictly use the format above and keep the answer concise. Only display the final output.

    <</SYS>

    <<SYS>>
    **Important** NOTE that if the phrase is a verb, use the form of the verb EXACTLY AS PROVIDED IN csv context.
    For example, if a sentence uses the phrase "Carrying", but the phrase provided in the csv context is "carry",
    then the phrase selected in the FINAL OUTPUT is "carry.mp4".
    Additionally, try including maximum verbs from the sentence in to the final output.
    For example, if the sentence is given as "The bee hits the donkey", then the phrases in the final output must include "bee", "hits" and "donkey".
    
    Additionally, keep only use the singular/plural form of a word provided in the context.
    For example, if the sentence is given as "The mother hits the child", then the phrases in the final output must include "mother", "hits" and "children", since "child" does not exist in the given csv context, but "children" does exist.

    DO NOT INVENT WORDS/PHRASES, strictly use the csv context provided.

    Try splitting the sentence to achieve maximum number of phrases, with each phrase having maximum no. of characters.
    <</SYS>>
    
    Sentence to translate: {question}
    Answer: [/INST]"""

    model = ChatOllama(
        model="llama2:7b-chat",
        num_gpu=1,
        temperature=0.01,
        top_k=10,
        top_p=0.5,
        verbose=False
    )

    print("Created the model object!")

    loader = CSVLoader(
        file_path="data/en-data.csv",
        csv_args={
            "delimiter": ",",
            "quotechar": '"',
            "fieldnames": ["phrase", "path"]
        },
        source_column="phrase"
    )
    print("Started data loading:")
    data = loader.load()

    #text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    #all_splits = text_splitter.split_documents(data)

    print("CSV ready to be embedded..")
    vectorstore = Chroma.from_documents(documents=data, embedding=GPT4AllEmbeddings())
    print("Embedding complete..")
    #question = "I love to swim in the swimming pool after painting"
    #question = 'I love to paint before swimming'
    #question = 'I love to play football at the sports union before painting'
    #question = 'The knife is playing basketball'
    docs = vectorstore.similarity_search(question)
    print("Similar documents:")
    print(docs)
    print("No. of similar documents:", len(docs))

    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=TEMPLATE,
    )

    qa_chain = RetrievalQA.from_chain_type(
        model,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )
    result = qa_chain({"query": question})
    print('\n\n')

    output_str: str = result['result']
    print(output_str)
    try:
        start_index = output_str.index('[')
        end_index = output_str.index(']') + 1
        output = eval(output_str[start_index: end_index])
    except Exception:
        start_index = output_str.index('{')
        end_index = output_str.index('}') + 1
        output: list[dict] = [eval(output_str[start_index: end_index])]
        for phrase_obj in output:
            if not phrase_obj['path'].startswith(VIDEO_DATA_PATH):
                phrase_obj['path'] = VIDEO_DATA_PATH + '/' + phrase_obj['path']

    for i in range(len(output)):
        with open('data/en-data.csv') as f:
            file = csv.DictReader(f)
        for row in file:
            if row['path'] == output[i]['path']:
                break
        else:
            arabic = get_arabic(output[i]['phrase'])

    return output

if __name__ == '__main__':
    #prediction = "I love to play football at the sports union before painting"
    prediction = "I am going hiking after swimming towards a well carrying a knife"
    #prediction = "The llama looked at the lion baking a cake in the oven in the swimming pool at the sports union after a painting session"
    output = get_prediction(prediction)
    print("Final Output:")
    print(json.dumps(output, indent=4))