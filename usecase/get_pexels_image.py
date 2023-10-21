import requests
import os
from dotenv import load_dotenv
load_dotenv()

PEXELS_KEY = os.getenv('PEXELS_KEY')

def get_pexels_images(keyword: str) -> list:
    base_url = "https://api.pexels.com/v1"
    endpoint = "/search"
    url = base_url + endpoint
    headers = {
    "Authorization": PEXELS_KEY
    }
    params={"query":keyword, "orientation":"portrait"}
    response = requests.get(url, headers=headers,params=params)

#we can display limit based on size
    if response.status_code == 200:
        data = response.json()
        urls = []
        for i in range(4):
            try:
                image_url = data.get("photos")[i].get("src").get('portrait')
                urls.append(image_url)
            except Exception:
                print("PexelsAPI error: ")
                print(i, data.get("photos"))
                break
        return urls


