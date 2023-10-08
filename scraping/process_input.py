from language import Language

def process_esl_data(language: Language):
    assert language in [member for member in Language], "Language not supported!"
    print(f"Processing data in ({language})")

    language = language.value
    data_file = f'data/{language}-data.txt'

    with open(data_file) as f:
        words = f.read().splitlines()

    unique = []
    for word in words:
        word = word.split(':')[0]
        if word not in unique:
            unique.append(word)
    print(unique)
    print("No. of resources:", len(unique))

if __name__ == '__main__':
    process_esl_data(Language.ARABIC)
        

    