from moviepy.editor import VideoFileClip

# Open the text file containing video links
with open('chinese-links.txt', 'r') as file:
    for i, line in enumerate(file):
       
            # Read video link and remove leading/trailing whitespace
            video_link = line.strip()

            # Load the downloaded video using MoviePy
            video = VideoFileClip(f"data/videos/{video_link}")

            # Get the dimensions of the video
            width, height = video.size

            # Calculate the new dimensions for cropping and resizing (central 50% width, 100% height)
            new_width = int(width * 0.5)
            new_height = height

            # Crop the video to the central 50% width and the same height
            cropped_video = video.crop(x1=0, y1=0, x2=width // 2, y2=height)

            # Resize the cropped video to the original height (100%)
            resized_video = cropped_video.resize(height=height)

            # Trim the video to the first 4 seconds
            trimmed_video = resized_video.subclip(0, 4)
            # Save the resized video with the original filename
            trimmed_video.write_videofile(f'data/cropped-chinese/{video_link}', codec='libx264')

            # Close the video objects
            video.close()
            cropped_video.close()
            resized_video.close()
