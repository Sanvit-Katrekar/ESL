from langchain.llms.ollama import Ollama
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain import hub
import warnings

warnings.filterwarnings('ignore')

def get_prediction(question: str) -> list[dict]:
    PROMPT = """
    [INST]
    <<SYS>>
    You are a sign language translator assistant.
    You will be given context of phrases mapped to a video link, of the format:

    "First Phrase: First phrase video link" i.e., the context contains phrase and link delimited by a ':'

    For example, first phrase = Today
    Today: https://player.vimeo.com/external/516074516.sd.mp4?s=5a74961fe7e2d7374401234ccc5a3b1f407fc790&profile_id=164&download=1

    Treat the above only as an example, do not use it in replies.

    Consider the part starting with "https://" as "video link"
    So that, "Today video link" will mean "https://player.vimeo.com/external/516074516.sd.mp4?s=5a74961fe7e2d7374401234ccc5a3b1f407fc790&profile_id=164&download=1

    Your vocabulary is strictly restricted to the phrases provided in:

    {context}

    The above phrases are also presented in the document, used for question answering.

    Omit all grammar rules such that:
    1. Assistant translates for a language restricted to the vocabulary provided above.
    2. Assistant translates for a language without prepositions and grammatical phrases.
    3. Make meaningful translations.
    4. Replace phrases in the sentence with their synonyms or closest matches from the provided vocabulary.
    5. No prepositions or grammatical phrases in the translation, the sentence is simplified to just the main phrases.
    6. In case the phrase does not exist in the vocabulary, replace with individual letters.
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

    Phrase strictly contains at most 2 words.
    Phrase should match exactly that of the phrase in the vocabulary provided as context.

    Strictly use the format above and keep the answer concise.

    <<SYS>>
    Sentence to translate: {question}
    Answer: 
    [/INST]"""


    model = Ollama(
        model="llama2",
        num_gpu=10,
        temperature=0.2,
        top_k=10,
        top_p=0.5
    )

    loader = TextLoader("data/en-data.txt")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)

    vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

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
        start_index = output_str.index('[')
        end_index = output_str.index(']') + 1
        output = eval(output_str[start_index: end_index])
    except:
        start_index = output_str.index('{')
        end_index = output_str.index('}') + 1
        output = [eval(output_str[start_index: end_index])]

    return output

if __name__ == '__main__':
    output = get_prediction("The Lion is swimming in the swimming pool")
    print(output)