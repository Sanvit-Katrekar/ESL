'''
from bs4 import BeautifulSoup

def scrape_yt_page():
    scrape_file = f'data/scraped-html/esl-zayed.html'

    with open(scrape_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    count = 0

    output_file = f'data/esl-zayed-data.txt'

    with open(output_file, 'w') as f:
        for video in soup.find_all('a'):
            if video.get('id') == 'thumbnail' and video.get('href'):
                link = video.get('href')
                if not link.startswith('/watch') or 'pp=' not in link:
                    continue
                f.write(f"www.youtube.com{link}\n")
                count += 1


    print("No. of resources:", count)

if __name__ == '__main__':
    scrape_yt_page()
'''

import json
YT_BASE = "https://www.youtube.com/watch?v="
def get_yt_links():
    scrape_file = f'data/scraped-html/esl-zayed.json'
    with open(scrape_file, 'r') as f:
        data = json.load(f)

    count = 0
    output_file = f'data/esl-zayed-data.txt'

    with open(output_file, 'w') as f:
        for video in data['items']:
            try:
                f.write(f"{video['snippet']['title']}: {YT_BASE}{video['id']['videoId']}\n")
            except:
                print(video)
                raise AssertionError("lol")
            count += 1

    print("No. of resources:", count)

if __name__ == '__main__':
    get_yt_links()

        

    
    