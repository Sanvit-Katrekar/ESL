from fastapi import FastAPI, BackgroundTasks

from constants import *
import uvicorn
from usecase.en_to_esl import convert_english_to_esl
from entity.response_model import Response, ResponseBase
from entity.request_model import VideoCreateRequest
from entity.status import Status
from entity.images import Images
from usecase.check_status import check_status
from usecase.get_pexels_image import get_pexels_images
import os, shutil
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

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
            "description": "Pass in English sentence to generate ESL video. This is an **async** call.",
        },
        {
            "name": "status",
            "description": "Check status of prediction request."
        }
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:9090"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test", response_model=dict, tags=["test"])
async def test() -> dict:
    return {"message": "API deployment successful!"}

@app.post("/predict", response_model=Response, tags=["predict"])
def english_to_esl(video_details: VideoCreateRequest, background_tasks: BackgroundTasks) -> Response:
    print("Generating a response:", video_details.english_sentence, "video_name: ", video_details.video_name)
    if not video_details.video_name:
        video_details.video_name = f"{str(uuid4())}.mp4"
    
    convert_english_to_esl(
        video_details.english_sentence,
        video_details.video_name
    )
    video_path = f'/{video_details.video_name}'
    response = Response(video_path=video_path)
    return response

@app.get("/get-status", response_model=ResponseBase, tags=["status"])
async def check_prediction_status(video_name: str) -> ResponseBase:
    print("Checking status of", video_name)
    status = check_status(video_name)
    return ResponseBase(**status)

@app.post("/get-images",response_model=ResponseBase, tags=["images"])
def get_images(keyword: str) ->Images :
    print("Checking status of", keyword)
    image_list = get_pexels_images(keyword)
    return (image_list)


@app.delete("/cleanup", response_model=ResponseBase, tags=["cleanup"])
def clean_up():
    n_videos = len(os.listdir(VIDEO_OUTPUT_PATH))
    shutil.rmtree(VIDEO_OUTPUT_PATH)
    os.mkdir(VIDEO_OUTPUT_PATH)
    return ResponseBase(message=f'{n_videos} videos cleaned up successfully!')


if __name__ == "__main__":
   uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
