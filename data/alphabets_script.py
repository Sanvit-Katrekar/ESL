with open('data/en-arabic-letters.txt') as f:
    letters = [letter.rstrip('\n') for letter in f.readlines()]

PATH = "data/videos"
with open('data/en-arabic-letters.csv', 'w') as f:
    f.write('alphabet,path\n')
    for letter in letters:
        f.write(f"{letter},{PATH}/{letter.replace(' ', '-')}.mp4\n")