from moviepy.editor import *
'''
from urllib.request import urlretrieve
from urllib.error import HTTPError
'''

import shutil
import ssl
from .final_llama2 import get_prediction
from uuid import uuid4

from constants import VIDEO_OUTPUT_PATH

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
 
def create_video(video_details: list[dict], video_name=f'{str(uuid4())}.mp4'):
    start = 0
    clips = []
    TEMP_FOLDER = 'tmp'
    if os.path.isdir(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)
    os.mkdir(TEMP_FOLDER)
    for video in video_details:
        '''
        name = f'tmp/video_{i}.mp4'
        try:
           urlretrieve(video['path'], name)
        except HTTPError:
           continue
        '''
        clip = VideoFileClip(video['path']).set_start(start)
        clip = clip.fx( vfx.resize, width=1280) 
        start += clip.duration
        clips.append(clip)
    shutil.rmtree(TEMP_FOLDER)

    final = CompositeVideoClip(clips)

    video_path = f'{VIDEO_OUTPUT_PATH}/{video_name}'
    final.write_videofile(video_path)
    return video_path

if __name__ == '__main__':
    # prediction = "I like to pay football at the sports union after painting"
    prediction = "I am going hiking after swimming towards a well carrying a knife"
    #prediction = "The Lion is swimming in the swimming pool while The oven is baking a cake."
    #prediction = "The llama looked at the lion baking a cake in the oven in the swimming pool at the sports union after a painting session"
    #prediction = "The Lion is swimming in the swimming pool while The Baker is baking a cake in the oven."
    #prediction = "The american army is angry".lower()
    output = get_prediction(prediction.lower())
    print(create_video(output))
    