import os

PATH = 'data/videos'
videos = os.listdir(PATH)

with open('data/en-data.csv', 'w') as f:
    f.write('phrase,path\n')
    for video in videos:
        f.write(f'{video.split(".")[0].replace("-", " ").lower()},{PATH}/{video}\n')