from moviepy.editor import *
from urllib.request import urlretrieve 
import shutil
import ssl
from final_llm import get_prediction

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
 
def create_video(video_details: list[dict]):
    start = 0
    clips = []
    TEMP_FOLDER = 'tmp'
    os.mkdir(TEMP_FOLDER)
    for i, video in enumerate(video_details):
       name = f'tmp/video_{i}.mp4'
       urlretrieve(video['link'], name)
       clip = VideoFileClip(name).subclip(0, 5).set_start(start)
       start += clip.duration
       clips.append(clip)
    shutil.rmtree(TEMP_FOLDER)
    # concatenating both the clips
    final = CompositeVideoClip(clips)
    #writing the video into a file / saving the combined video
    final.write_videofile("merged.mp4")

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
    output = get_prediction("The Lion is swimming in the swimming pool")
    create_video(output)

