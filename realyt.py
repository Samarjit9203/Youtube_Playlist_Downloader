import os
import time
from pytube import Playlist, YouTube

# Replace with the Desired URL of the Playlist
playlist_url = ''

# Replace with the Desired location to save
save_path = r''

#Creating a Playlist object
playlist = Playlist(playlist_url)

#Initializing a counter to Download and rename Serially
counter = 1

#Iterating through each video in the playlist
for video_url in playlist.video_urls:
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        file_name = f"{counter}) {yt.title}"
        video_stream.download(output_path=save_path, filename=str(counter))
        os.rename(os.path.join(save_path, f"{counter}.mp4"), os.path.join(save_path, f"{counter}) {yt.title}.mp4"))
        print(f'File downloaded as: {file_name}.mp4')
        counter += 1

        # Add a short delay to avoid overloading the server
        time.sleep(2)

    except Exception as e:
        print(f'Error downloading video {counter}: {str(e)}')

#Printing a message for Confirmation that all Videos downloaded Successfully
print("All videos downloaded successfully")
