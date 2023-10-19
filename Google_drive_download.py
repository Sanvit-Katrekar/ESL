import requests

# Google Drive folder link (publicly shared folder)
folder_link = "https://drive.google.com/drive/folders/1oImwzXGLhlxKU6If-5jp_9ui_a5oJFib"

# List of file names to download
file_names = ["Beach.mp4"]
#, "Build.mp4", "Clean.mp4"

# Destination folder for downloaded files
destination_folder = "data/videos/download_gdrive"

for file_name in file_names:
    # Construct the direct download link for the file
    direct_download_link = f"{folder_link}/file/{file_name}"

    # Send a request to Google Drive to get the direct download link
    response = requests.get(direct_download_link, allow_redirects=False)
    '''
    # Extract the direct download link from the response headers
    direct_download_link = response.headers["Location"]

    # Download the file
    response = requests.get(direct_download_link)

    # Save the file to the destination folder
    with open(destination_folder + file_name, "wb") as file:
        file.write(response.content)
    '''
    print(response.content)
    #print(response.content['Report-To'])
    #print(f"Downloaded: {file_name}")

print("All files downloaded successfully.")

