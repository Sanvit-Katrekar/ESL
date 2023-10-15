from moviepy.editor import *
from urllib.request import urlretrieve 

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
 
def create_video(video_details: list[dict]):
    start = 0
    clips = []
    for i, video in enumerate(video_details):
       name = f'video_{i}.mp4'
       urlretrieve(video['link'], name)
       clip = VideoFileClip(name).subclip(0, 5)
       start += clip.duration
       clips.append(clip)
    # concatenating both the clips
    final = CompositeVideoClip(clips)
    #writing the video into a file / saving the combined video
    final.write_videofile("merged.mp4")

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

