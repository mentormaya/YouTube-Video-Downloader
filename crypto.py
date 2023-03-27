from io import BytesIO
import json
from pprint import pprint
from pytube import YouTube, Playlist, Stream

url = 'https://www.youtube.com/watch?v=X0Akv2AYvbw'

yt = YouTube(url)

name = yt.title

stream = yt.streams.get_highest_resolution()

pprint(stream)

# with open('streams.json', 'w') as streams:
#     streams.write(json.dumps(yt.streaming_data))

stream_buffer = BytesIO
stream.stream_to_buffer(stream_buffer)

with open(name + ".mp4", 'wb') as video_buffer:
    video_buffer.write(stream_buffer.getbuffer())