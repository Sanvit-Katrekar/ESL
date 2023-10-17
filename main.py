from fastapi import FastAPI

from constants import *
import uvicorn
from usecase.en_to_esl import get_prediction, create_video
from entity.response_model import Response
from entity.request_model import VideoCreateRequest

app = FastAPI(
    title="English to ESL",
    description="""
    API to generate an ESL video from given English sentence.
    
    HTTP Exceptions - 400 and 401 are used to indicate invalid inputs. 500 indicates error in the API code.
    """,
    openapi_tags=[
        {
            "name": "test",
            "description": "Test for successful API deployment."
        },
        {
            "name": "predict",
            "description": "Pass in English sentence to generate ESL video. This is an **sync** call.",
        },
    ],
)

@app.get("/test", response_model=dict, tags=["test"])
async def test() -> dict:
    return {"message": "API deployment successful!"}

@app.post("/predict", response_model=Response, tags=["predict"])
async def english_to_esl(video_details: VideoCreateRequest) -> Response:
    print("Waiting for response:", video_details.english_sentence)
    '''
    video_path = convert_english_to_esl(video_details.english_sentence)
    response = Response(video_path=video_path)
    print("Got response!")
    return response'''

    prediction = "The American Army is Angry"
    output = get_prediction(prediction)
    print(create_video(output))

if __name__ == "__main__":
   uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
