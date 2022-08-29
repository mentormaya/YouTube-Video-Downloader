import json
import threading
from dotenv import dotenv_values
from pytube import YouTube, Playlist

#-----------------------------------------------
# local Library
#-----------------------------------------------
from libs.PythonJson import PythonJson as Pjson     #could be used from dotmap import DotMap

config = Pjson(dotenv_values(".env"))

class Downloader():
    def __init__(self):
        self.config = config
        self.url = str(self.config.URL)
        self.output_folder = str(self.config.OUTPUT_FOLDER)
        self.resolution = 'highest'
        self.multi_threading = bool(self.config.MULTITHREADING) if self.config.MULTITHREADING else False
    
    def get(self, url = None):
        if url is not None:
            self.url = str(url)
        self.yt = Playlist(self.url)
        self.title = self.yt.title
        self.total_videos = len(self.yt.videos)
        print(self.total_videos)
        
    def select_resolution(self, video):
        for index, stream in enumerate(video.streams):
            print(f'{index}. {stream.mime_type.split("/")[1]} {stream.resolution}')
        res = input("Choose the quality?")
        print(f'Video {video.title} ({video.streams[res].mime_type.split("/")[1]} {video.streams[res].resolution}) is selected...')
        return video.streams[res]
            
    def get_highest_resolution(self, video):
        print(f'Highest Resolution: {video.streams.get_highest_resolution().resolution} ({video.streams.get_highest_resolution().mime_type.split("/")[1]}) for {video.title} is selected...')
        return video.streams.get_highest_resolution()

    def get_stream(self, video, resolution):
        if resolution == 'highest':
            return self.get_highest_resolution(video)
        if resolution == 'select':
            return self.select_resolution(video)
        #TODO for other resolutions

    def download(self, out_path = None, resolution = 'highest'):
        if out_path is not None:
            self.output_folder = str(out_path)
        self.resolution = resolution
        if self.total_videos > 1:
            full_out_location = self.output_folder + "/" + self.title + "/"
        else:
            full_out_location = self.output_folder + "/"
        if self.multi_threading:
            print('Multi Threading On...')
        # for video in self.yt.videos:
        #     self.save(video, full_out_location)
        print(f"All the downloads Completed Successfully and Saved to {full_out_location}")
    
    def save(self, video, path):
        self.get_stream(video, self.resolution).download(path)