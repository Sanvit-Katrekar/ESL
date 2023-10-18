'''
import os
import openai
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Set your Azure Key Vault details
keyvault_name = "your_keyvault_name"
secret_name = "your_secret_name"
azure_endpoint = "https://your_keyvault_name.vault.azure.net/"

# Get the Azure Key and Endpoint from your Azure Key Vault
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=azure_endpoint, credential=credential)

azure_key = secret_client.get_secret(secret_name).value

# Set your OpenAI API details
openai.api_key = azure_key
openai.api_version = "v1"  # Change to the appropriate version

# Set the engine type (davinci, curie, etc.)
engine = "davinci"  # Change this to your desired engine

# Your text prompt
text_prompt = "Translate the following English text to French: 'Hello, world.'"

# Generate text completion using OpenAI GPT-3 via Azure
response = openai.Completion.create(
    engine=engine,
    prompt=text_prompt,
    max_tokens=50  # Adjust this as needed
)

# Extract and print the generated text
generated_text = response.choices[0].text
print("Generated Text: ", generated_text)
'''

from langchain.chat_models import ChatOllama
from langchain.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain.prompts import PromptTemplate
import warnings
import json

warnings.filterwarnings('ignore')

def get_prediction(question: str) -> list[dict]:
    TEMPLATE = """
    [INST]
    <<SYS>>
    You are a conversion assistant that helps convert english word to individual "alphabets" of a language.

    Given word is converted into individual "alphabets" of the language.
    The individual "alphabets" in the language is given below int the form of a csv context:

    {context}

    ONLY USE THE ALPHABETS PROVIDED ABOVE.

    Final Answer should strictly be of the form:
    [
        {{
            "alphabet": Alphabet selected from the csv context provided,
            "path": Path to the alphabet selected from csv context provided.
        }}
    ]

    <</SYS>>
    Sentence to translate: {question}
    Final Answer: [/INST]"""

    model = ChatOllama(
        model="llama2:7b-chat",
        num_gpu=1,
        temperature=0.01,
        top_k=10,
        top_p=0.5,
        verbose=False
    )

    loader = CSVLoader(
        file_path="data/en-arabic-letters.csv",
        csv_args={
            "delimiter": ",",
            "quotechar": '"',
            "fieldnames": ["alphabet", "path"]
        },
        source_column="alphabet"
    )
    data = loader.load()

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
        start_index = output_str.index('[')
        end_index = output_str.index(']') + 1
        output = eval(output_str[start_index: end_index])
    except:
        start_index = output_str.index('{')
        end_index = output_str.index('}') + 1
        output = [eval(output_str[start_index: end_index])]

    return output

if __name__ == '__main__':
    #prediction = "I love to play football at the sports union before painting"
    prediction = "baking"
    #prediction = "The llama looked at the lion baking a cake in the oven in the swimming pool at the sports union after a painting session"
    output = get_prediction(prediction)
    print("Final Output:")
    print(json.dumps(output, indent=4))