from db_engine import engine
from tables import ESL
from sqlmodel import SQLModel, Session

SQLModel.metadata.create_all(engine)

count = 0
try:
    with Session(engine) as session:
        with open('data/en-data.txt') as f:
            words = f.read().splitlines()
        total = len(words)
        for word in words:
            word, link = [s.strip() for s in word.split(':', 1)]
            esl_word = ESL(en_word=word, video_link=link)
            session.add(esl_word)
            session.commit()
            count += 1
            print(f'Progress: {round(count/total * 100, 2)}% | {count} records')
except:
    print('No. of records added:', count)
    raise Exception('Disconnecting with database..')
