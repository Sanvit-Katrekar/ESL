from .get_arabic import get_arabic

def convert(output: list[dict]):
    try:
        print("Entering loop")
        print("Starting check:", output)
        arabic = ''
        with open('data/en-data.csv') as f:
            file = f.read().splitlines()[1:]
        with open('data/en-arabic-letters.csv') as g:
            alphabets_file = g.read().splitlines()[1:]
        to_replace = []
        for i in range(len(output)):
            for line in file: # Checks for file existing
                phrase, path = line.split(',')
                if path == output[i]['path']:
                    break
            else: # Get arabic letters
                letters = []
                arabic = get_arabic(output[i]['phrase'])['translation'].replace(' ', '')
                for letter in arabic:
                    for line in alphabets_file:
                        alphabet, path = line.split(',')

                        if alphabet == letter:
                            letters.append({"phrase": alphabet, "path": path})
                            break
                to_replace.append(dict(letters=letters, index=i))
        
        str_output = str(output)
        for replacement in to_replace:
            print("initial output:")
            print(str_output)
            str_replacement = str(replacement['letters']).lstrip('[').rstrip(']')
            print("replacement:")
            print(str_replacement)
            str_to_replace = str(output[replacement['index']])
            print("to replace:")
            print(str_to_replace)
            str_output = str_output.replace(str_to_replace, str_replacement)
        return eval(str_output)
    except Exception as e:
        print("Error:", e)
        print('arabic', arabic)
        output['path'] = 'data/videos/About.mp4'
        return output
    

