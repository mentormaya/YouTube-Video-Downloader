import json
from dotenv import dotenv_values
from pytube import YouTube, Playlist

output_folder = "F:/YoutubeVideos"

config = dotenv_values(".env")
# v_url = "https://www.youtube.com/watch?v=JeznW_7DlB0"

# list_url = "https://www.youtube.com/playlist?list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-"

url = config

def print_streams(streams):
    for index, stream in enumerate(streams):
        print(f'{index}. {stream.mime_type.split("/")[1]} {stream.resolution}')

if "playlist"  in url:
    is_list = True
    yt = Playlist(url)
else:
    is_list = False
    yt = YouTube(url)

if is_list:
    topic = yt.title
    full_out_location = output_folder + "/" + topic + "/"
    for video in yt.videos:
        print(f'Highest Resolution: {video.streams.get_highest_resolution().resolution} {video.streams.get_highest_resolution().mime_type.split("/")[1]} for {video.title} is Downloading...')
        video.streams.get_highest_resolution().download(full_out_location)
else:
    full_out_location = output_folder + "/"
    print_streams(yt.streams)    
    res = input("Choose the quality?")
    res = int(res)
    print(f'Video {yt.title} ({yt.streams[res].mime_type.split("/")[1]} {yt.streams[res].resolution}) is downloading...')
    full_out_location = yt.streams[res].download(full_out_location)

print(f"All the downloads Completed Successfully and Saved to {full_out_location}")