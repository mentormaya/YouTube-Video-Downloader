import json
from threading import Thread
from dotenv import dotenv_values
from pytube import YouTube, Playlist

#-----------------------------------------------
# local Library
#-----------------------------------------------
from libs.PythonJson import PythonJson as Pjson     #could be used from dotmap import DotMap

config = Pjson(dotenv_values(".env"))

class GetInfo(Thread):
    def __init__(self, url = None, status = None):
        super().__init__()
        self.status = status
        self.downloader = Downloader(self.status)
        self.url = url
    
    def run(self):
        self.info = self.downloader.get(self.url)
        self.info.status = self.status
        self.update(f'GotInfo: {self.downloader.title}')
    
    def update(self, msg):
        if self.status is not None:
            self.status.updateStatus(msg)
        else:
            print(msg)

class Download(Thread):
    def __init__(self, yt, out_path = None, resolution = 'highest'):
        super().__init__()
        self.downloader = yt
        self.status = yt.status
        self.out_path = out_path
        self.resolution = resolution
    
    def run(self):
        self.update(f'Downloading: {self.downloader.title}')
        self.downloader.download(self.out_path, self.resolution)
    
    def update(self, msg):
        if self.status is not None:
            self.status.updateStatus(msg)
        else:
            print(msg)
class Downloader():
    def __init__(self, status):
        self.config = config
        self.status = status
        self.url = str(self.config.URL)
        self.output_folder = str(self.config.OUTPUT_FOLDER)
        self.resolution = 'highest'
        self.multi_threading = bool(self.config.MULTITHREADING) if self.config.MULTITHREADING else False
    
    def update(self, msg):
        if self.status is not None:
            self.status.updateStatus(msg)
        else:
            print(msg)
    
    def get(self, url = None):
        if url is not None:
            self.url = str(url)
        if 'playlist' in self.url:
            self.yt = Playlist(self.url)
            self.total_videos = self.yt.length
        else:
            self.yt = YouTube(self.url)
            self.total_videos = 1
        self.title = self.yt.title
        return self
        
    def select_resolution(self, video):
        for index, stream in enumerate(video.streams):
            self.update(f'{index}. {stream.mime_type.split("/")[1]} {stream.resolution}')
        res = input("Choose the quality?")
<<<<<<< HEAD
        print(f'Video {video.title} ({video.streams[res].file_extension } - {video.streams[res].type} {video.streams[res].resolution}) is selected...')
        return video.streams[res]
            
    def get_highest_resolution(self, video):
        print(f'Highest Resolution: {video.title} ({video.streams.get_highest_resolution().file_extension } - {video.streams.get_highest_resolution().type} {video.streams.get_highest_resolution().resolution}) is selected...')
=======
        self.update(f'Resolution: {video.streams[res].resolution} ({video.streams.get_highest_resolution().subtype} - {video.streams.get_highest_resolution().type}) for {video.title} is selected...')
        return video.streams[res]
            
    def get_highest_resolution(self, video):
        self.update(f'Highest Resolution:  {video.streams.get_highest_resolution().resolution} ({video.streams.get_highest_resolution().subtype} - {video.streams.get_highest_resolution().type}) for {video.title} is selected...')
>>>>>>> 96c3a7902d8df9c71312f6b29d9d5f90dbf3fd89
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
        full_out_location = self.output_folder + "/"
        if self.total_videos > 1:
            full_out_location += self.title + "/"
        elif 'CID' in self.title:
            full_out_location += "CID" + "/"
        elif 'Crime Patrol' in self.title:
            full_out_location += "Crime Patrol" + "/"
        else:
            full_out_location = self.output_folder + "/"
<<<<<<< HEAD
        if self.total_videos > 1:
            if self.multi_threading:
                print('Multi Threading On...')
            for video in self.yt.videos:
                self.save(video, full_out_location)
        else:
            self.save(self.yt,full_out_location)
=======
        if (self.total_videos > 1):
            self.save_all(self.yt.videos, full_out_location)
        else:
            self.save(self.yt, full_out_location)
>>>>>>> 96c3a7902d8df9c71312f6b29d9d5f90dbf3fd89
        print(f"All the downloads Completed Successfully and Saved to {full_out_location}")
    
    def save(self, video, path):
        self.get_stream(video, self.resolution).download(path)
    
    def save_all(self, videos, path):
        for video in videos:
            self.get_stream(video, self.resolution).download(path)