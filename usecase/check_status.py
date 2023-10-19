import os
from constants import VIDEO_OUTPUT_PATH
from entity.status import Status

def check_status(video_name: str) -> dict:
    ''' Returns status response dict '''
    if '/' in video_name:
        file_name = video_name.split('/')[-1]
    else:
        file_name = video_name
    output_files = os.listdir(VIDEO_OUTPUT_PATH)
    if file_name in output_files:
        status = Status.COMPLETE
        message = "prediction complete, video generated"
        return {"status": status.value, "message": message}
        
    name_without_ext = file_name.split('.')[0]
    error_file = f'{name_without_ext}-error.txt'
    if error_file in output_files:
        status = Status.ERROR
        with open(f'{VIDEO_OUTPUT_PATH}/{error_file}') as f:
            error = f.read()
        message = "An error occured: " + error
    else:
        status = Status.IN_PROGESS
        message = "prediction in progress"
    return {"status": status.value, "message": message}
    