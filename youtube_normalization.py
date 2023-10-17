import os

# Define the path to your folder
folder_path = "youtube_videos/"
'''
# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".mp4"):
        # Replace spaces with hyphens in the filename
        new_filename = filename.replace(" ", "-")

        # Generate the full file paths
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_filepath, new_filepath)

        # Check if the file has been successfully renamed
        if os.path.exists(new_filepath):
            print(f"Renamed '{filename}' to '{new_filename}'")
        else:
            print(f"Failed to rename '{filename}' to '{new_filename}'")


'''
for filename in sorted(os.listdir(folder_path)):
    if filename.endswith(".mp4"):
        # Get the part before ".mp4" and store it in the 'title' variable
        
        #print(title.replace("-", " ")+f": youtube_videos/{filename}")
        print(filename)
