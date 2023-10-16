from langchain.chat_models import ChatOllama
from langchain.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain.prompts import PromptTemplate
import warnings
import json

from langchain.callbacks import get_openai_callback

warnings.filterwarnings('ignore')

def get_prediction(question: str) -> list[dict]:
    TEMPLATE = """
    [INST]
    <<SYS>>
    
    You are a sign language translator assistant.
    You will be given context of a CSV file, where in 'phrase' and 'video link to the respective phrase' are attributes.

    Your vocabulary is STRICTLY RESTRICTDED to the phrases provided, use the following pieces of context to translate the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    {context}

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
    [
    {{
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

    <</SYS>>
    Sentence to translate: {question}
    Answer: [/INST]"""

    model = ChatOllama(
        model="llama2:7b-chat",
        num_gpu=1,
        temperature=0.2,
        top_k=10,
        top_p=0.5,
        verbose=True
    )

    loader = CSVLoader(
        file_path="data/en-data.csv",
        csv_args={
            "delimiter": ",",
            "quotechar": '"',
            "fieldnames": ["phrase", "link"]
        },
        source_column="link"
    )
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    all_splits = text_splitter.split_documents(data)

    print("CSV ready to be embedded..")
    vectorstore = Chroma.from_documents(documents=data, embedding=GPT4AllEmbeddings())
    print("Embedding complete..")
    #question = "I love to swim in the swimming pool after painting"
    #question = 'I love to paint before swimming'
    #question = 'I love to play football at the sports union before painting'
    #question = 'The knife is playing basketball'
    docs = vectorstore.similarity_search(question)
    print("No. of docs:", docs)
    '''

    rag_prompt_llama = hub.pull("rlm/rag-prompt-llama")
    rag_prompt_llama.messages[0].prompt.template = PROMPT

    chain = load_qa_chain(model, chain_type="stuff", prompt=rag_prompt_llama)

    with get_openai_callback() as cb:
        result = chain({"input_documents": docs, "question": question}, return_only_outputs=False)
        print("Tokens used:", cb)
    '''

    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=TEMPLATE,
    )

    from langchain.chains import RetrievalQA
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
        start_index = output_str.index('{')
        end_index = output_str.index(']') + 1
        output = eval('[' + output_str[start_index: end_index])
    except:
        start_index = output_str.index('{')
        end_index = output_str.index('}') + 1
        output = [eval(output_str[start_index: end_index])]

    return output

if __name__ == '__main__':
    output = get_prediction("I love to play football at the sports union before painting")
    print("Final Output:")
    print(json.dumps(output, indent=4))