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
    # prediction = "I like to play football at the sports union after painting" "/c1361ae4-ea32-4b95-a53c-94a7ec942496.mp4"
    prediction = "I am going hiking after swimming towards a well carrying a knife" #"/5f0d3a93-f639-4ac4-97bd-cc0fbd273f86.mp4"
    #prediction = "The llama looked at the lion baking a cake in the oven in the swimming pool at the sports union after a painting session" "/e6512107-02df-41c0-95b3-967a5b448010.mp4"
    #prediction = "The Lion is swimming in the swimming pool while The Baker is baking a cake in the oven." "/4ac19ba7-9311-42fe-9791-0e1263604fcf.mp4"
    #prediction = "The american army is angry" "/5a7865a6-82f3-479d-a001-ae7c3e04f1f1.mp4"
    #prediction = "Heramb is playing guitar" /86d4dbee-eb57-404d-a607-19d414226891.mp4
    #prediction = "Sanvit is watering the flowers" "/ab6e145e-337f-4b22-bbd8-506e4f3d0294.mp4"
    #prediction = "Bhavya is a programmer" "/b221c0f8-0800-46d1-a2b7-19c655b83099.mp4"
    output = get_prediction(prediction.lower())
    print(create_video(output))
    