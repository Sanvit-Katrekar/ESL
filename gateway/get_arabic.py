from langchain.chat_models import ChatOllama
from langchain.document_loaders import CSVLoader
from langchain.schema import HumanMessage, SystemMessage
import warnings

#VIDEO_DATA_PATH = 'data/videos'

warnings.filterwarnings('ignore')

def get_arabic(phrase: str) -> list[dict]:

    model = ChatOllama(
        model="llama2:7b-chat",
        num_gpu=2,
        temperature=0.01,
        top_k=10,
        top_p=0.5,
        verbose=False
    )
    prompt = f'Translate the phrase "{phrase}".'
    messages = [
        SystemMessage(content='You are a english to arabic translating assistant.'),
        HumanMessage(content=prompt),
        SystemMessage(content='STRICTLY give the translation as the final output, in the form of {"translation": Translated text}')
    ]
    return eval(model(messages).content)

if __name__ == '__main__':
    print(get_arabic('sanvit'))
 