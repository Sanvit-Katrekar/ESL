from pytube import YouTube
from uuid import uuid4
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

BASE_PATH = 'data/esl_zayed'

def download_video_from_youtube(link, path):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    # download the video
    video.download(path)

if __name__ == '__main__':
    with open('data/esl-zayed-data.txt') as f:
        data = f.read().splitlines()
    for line in data:
        title, link = line.split(': ')
        if title.isascii():
            title = title.replace('-', '').replace(' ', '-')
        else:
            title = str(uuid4()) 
        download_video_from_youtube(link, f"{BASE_PATH}")
        print(f"Downloaded {title}.mp4")
