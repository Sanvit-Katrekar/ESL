import requests
from moviepy.editor import VideoFileClip
import os
# URL of the video you want to download
video_url = "https://example.com/your_video.mp4"
c=0
links = []

with open("data/en-data.txt", "r") as f:
    for i, line in enumerate(f):
        if i==58:
            split = line.split(":", maxsplit=1)
            if len(split) == 2:
                key = split[0].strip()
                value = split[1].strip()
                #print("Key:", key)
                #print("Value:", value)
                pair = [key, value]  # Create a list [key, value]
                links.append(pair)  # Append the list to the main array

# Now 'links' contains a list of key-value pairs as lists
#print(links)



# Create a directory to save the downloaded videos (if it doesn't exist)
if not os.path.exists("downloaded_videos"):
    os.makedirs("downloaded_videos")

for item in links:
    title = item[0]
    link = item[1]

    # Replace spaces with hyphens in the title
    title = title.replace(" ", "-")
    title = title.replace("/", "-")
    # Create the filename by appending ".mp4" to the title
    filename = f"data/videos/{title}.mp4"

    # Download and save the video with the filename
    response = requests.get(link)
    if response.status_code == 200:
        with open(filename, "wb") as video_file:
            video_file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}. Status code:", response.status_code)

'''
import requests
import os

# Define a dictionary with links and corresponding keys
links_and_keys = {
    "key1": "https://example.com/video1.mp4",
    "key2": "https://example.com/video2.mp4",
    "key3": "https://example.com/video3.mp4",
    # Add more key-value pairs as needed
}

# Create a directory to save the downloaded videos (if it doesn't exist)
if not os.path.exists("downloaded_videos"):
    os.makedirs("downloaded_videos")

# Download and save the videos
for key, link in links_and_keys.items():
    response = requests.get(link)
    if response.status_code == 200:
        filename = f"downloaded_videos/{key}.mp4"
        with open(filename, "wb") as video_file:
            video_file.write(response.content)
        print(f"Downloaded {key}.mp4")
    else:
        print(f"Failed to download {key}. Status code:", response.status_code)
'''

'''
# Send a GET request to the video URL
response = requests.get(video_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the video content to a file
    with open("downloaded_video.mp4", "wb") as video_file:
        video_file.write(response.content)
    print("Video downloaded successfully.")

    # Load the downloaded video with MoviePy
    video = VideoFileClip("downloaded_video.mp4")

    # You can now perform editing or other operations on the video if needed
    # For example, cropping or adding effects

    # Close the video object
    video.close()

else:
    print("Failed to download the video. Status code:", response.status_code)
'''