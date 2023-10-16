'''
with open('data/en-data.txt') as f:
    data = f.read()

with open('data/en-data.csv', 'w') as f:
    f.write('phrase,link\n')
    f.write(data.replace(': ', ','))
'''

from langchain.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import GPT4AllEmbeddings

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)

loader = CSVLoader(
    file_path="data/en-data.csv",
    csv_args={
        "delimiter": ",",
        "quotechar": '"',
        "fieldnames": ["phrase", "link"]
    },
    source_column="phrase"
)
data = loader.load()


all_splits = text_splitter.split_documents(data)

print(all_splits)

#vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())


