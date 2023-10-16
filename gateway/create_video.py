from moviepy.editor import *

from urllib.request import urlretrieve
from urllib.error import HTTPError
import shutil
import ssl
from .final_llm import get_prediction
from uuid import uuid4

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
    for i, video in enumerate(video_details):
        name = f'tmp/video_{i}.mp4'
        try:
           urlretrieve(video['link'], name)
        except HTTPError:
           continue
        clip = VideoFileClip(name).subclip(0, 5).set_start(start)
        start += clip.duration
        clips.append(clip)
    shutil.rmtree(TEMP_FOLDER)
    # concatenating both the clips
    final = CompositeVideoClip(clips)
    #writing the video into a file / saving the combined video
    video_path = f'output_videos/{video_name}'
    final.write_videofile(video_path)
    return video_path

if __name__ == '__main__':
    '''
    create_video(
    [{
        "phrase": "Play",
        "link": "https://player.vimeo.com/external/267630082.sd.mp4?s=cedc04d2f744731ef0c009efac27db351cd7e8c9&profile%20id=164&download=1"
    }, {
        "phrase": "Sports union",
        "link": "https://player.vimeo.com/external/267628422.sd.mp4?s=b05d2bb6228028d989fdde90d248292636f06d87&profile%20id=164&download=1"
    }, {
        "phrase": "Painting",
        "link": "https://player.vimeo.com/external/267523909.sd.mp4?s=939eda40b3188d6b4bcfbef2e5889d6e3a7a3e61&profile_id=164&download=1"
    }]  
    )
    '''
    '''
    video = create_video([
        {
            "phrase": "Closest matching phrase for 'pay'",
            "link": "https://player.vimeo.com/external/267630082.sd.mp4?s=cedc04d2f744731ef0c009efac27db351cd7e8c9&profile%20id=164&download=1"
        },
        {
            "phrase": "Closest matching phrase for 'football'",
            "link": "https://player.vimeo.com/external/267635798.sd.mp4?s=767f795d3f5cd1d29431f30c59457b96049099f5&profile%20id=164&download=1"
        },
        {
            "phrase": "Closest matching phrase for 'sports union'",
            "link": "https://player.vimeo.com/external/267627052.sd.mp4?s=93efeafd53e99e65fbdaf11193183a5cdec07f35&profile%20id=164&download=1"
        },
        {
            "phrase": "Closest matching phrase for 'painting'",
            "link": "https://player.vimeo.com/external/267448749.sd.mp4?s=1a742d950c9344b6ac8e7b47a78c2f7a93a0f53&profile%20id=164&download=1"
        }
    ])'''
    # prediction = "I like to pay football at the sports union after painting"
    # prediction = "I am going hiking after swimming towards a water well carrying a knife"
    #prediction = "The Lion is swimming in the swimming pool while The oven is baking a cake."
    prediction = "The llama looked at the lion baking a cake in the oven in the swimming pool at the sports union after a painting session, and the felt like playing football"
    output = get_prediction(prediction)
    print(create_video(output))
    