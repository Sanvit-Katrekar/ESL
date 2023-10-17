from gateway.final_llm import get_prediction
from gateway.create_video import create_video

def convert_english_to_esl(english_sentence: str) -> str:
    print("----Waiting for prediction----")
    prediction = get_prediction(english_sentence)
    print("----Gotem prediction----")
    video_path = create_video(prediction)
    return video_path
    
    