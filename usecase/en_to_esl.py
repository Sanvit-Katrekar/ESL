from gateway.final_llama2 import get_prediction
from gateway.create_video import create_video
from constants import *

def convert_english_to_esl(english_sentence: str, video_name: str) -> str:
    english_sentence = english_sentence.lower()
    if not video_name.endswith('.mp4'):
        video_name = video_name.rstrip('.') + '.mp4'
    video_path = VIDEO_DATA_PATH + '/' + video_name
    try:
        print("----Waiting for prediction----")
        prediction = get_prediction(english_sentence)
        print("----Prediction complete----")
        print("----Waiting for video generation----")
        create_video(prediction, video_name=video_name)
        print("----Video generation complete----")
    except Exception as e:
        error_file = f"{VIDEO_OUTPUT_PATH}/{video_name.split('.')[0]}-error.txt"
        with open(error_file, 'w') as f:
            f.write(str(e))
    return video_path
    
    