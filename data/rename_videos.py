import os

def normalize_video_names(path):
    for video in os.listdir(path):
        os.rename(path + video, path + video.replace(' ', '-').lower())

if __name__ == '__main__':
    # path = 'data/esl_zayed/'
    path = 'data/videos/'
    normalize_video_names(path)