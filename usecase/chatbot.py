from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage, SystemMessage
import re
import warnings

 
warnings.filterwarnings('ignore')

CONVERSATION_HISTORY = 'data/conversation/convo.txt'

chat_model = ChatOllama(model="llama2:7b-chat")

#conversation = ConversationChain(llm=chat_model)

with open(CONVERSATION_HISTORY) as f:
    history = f.read()

print(history)
query = input("What is your name?")


messages = [
    SystemMessage(content=f'''
        The following is a friendly conversation between a human and an AI.
        The AI is talkative and provides lots of specific details from its context.
        If the AI does not know the answer to a question, it truthfully says it does not know.
        However, the AI is limited to answer within 20 words.

        Current conversation:
        {history}
        '''
    ),
    HumanMessage(content=f'Human: {input}')
]
reply = chat_model(messages).content
reply = re.sub(r'\*([^*]+)\*', '', input)
print(reply)

with open(CONVERSATION_HISTORY, 'a') as f:
    f.write(f"Human: {query}\nAI: {reply}\n")

