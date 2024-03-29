import re
import os, sys
from tqdm.auto import tqdm
from threading import Thread
from dotenv import dotenv_values
from pytube import YouTube, Playlist, Stream

#-----------------------------------------------
# local Library
#-----------------------------------------------
from libs.PythonJson import PythonJson as Pjson     #could be used from dotmap import DotMap

extDataDir = os.getcwd()
if getattr(sys, 'frozen', False):
    extDataDir = sys._MEIPASS
config = Pjson(dotenv_values(os.path.join(extDataDir, '.env')))

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
        self.stream = None
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
            self.total_videos = len(self.yt.videos)
        else:
            self.yt = YouTube(self.url, on_progress_callback = self.updateProgress)
            self.total_videos = 1
        self.title = self.yt.title
        return self
    
    def updateProgress(self, stream: Stream, data_chunk: bytes, bytes_remaining: int):
        self.progressbar.update(len(data_chunk))
    
    def select_resolution(self, video):
        for index, stream in enumerate(video.streams):
            self.update(f'{index}. {stream.mime_type.split("/")[1]} {stream.resolution}')
        res = input("Choose the quality?")
        self.update(f'Resolution: {video.streams[res].resolution} ({video.streams.get_highest_resolution().subtype} - {video.streams.get_highest_resolution().type}) for "{video.title}" is selected...')
        return video.streams[res]
            
    def get_highest_resolution(self, video):
        self.update(f'Highest Resolution:  {video.streams.get_highest_resolution().resolution} ({video.streams.get_highest_resolution().subtype} - {video.streams.get_highest_resolution().type}) for "{video.title}" is selected...')
        return video.streams.get_highest_resolution()

    def get_stream(self, video, resolution):
        if resolution == 'highest':
            return self.get_highest_resolution(video)
        if resolution == 'select':
            return self.select_resolution(video)
        #TODO for other resolutions

    def sanitizeName(self, name):
        names = re.split(r'[`!;:|.<>?~]', name)
        for nm in names:
            name = re.sub(' +', ' ', nm).strip()
            if len(name) >= 5:
                break
        if len(name) > 25:
            name = name[:25]
        # print(f'Folder Name: {name}')
        return name
    
    def download(self, out_path = None, resolution = 'highest'):
        if out_path is not None:
            self.output_folder = str(out_path)
        self.resolution = resolution
        full_out_location = self.output_folder + "/"
        if self.total_videos > 1:
            full_out_location += self.sanitizeName(self.title) + "/"
        elif 'CID' in self.title:
            full_out_location += "CID" + "/"
        elif 'Crime Patrol' in self.title:
            full_out_location += "Crime Patrol" + "/"
        else:
            full_out_location = self.output_folder + "/"
        if (self.total_videos > 1):
            self.save_all(self.yt.videos, full_out_location)
        else:
            self.save(self.yt, full_out_location)
        print(f"All the downloads Completed Successfully and Saved to {full_out_location}")
    
    def save(self, video, path):
        self.stream = self.get_stream(video, self.resolution)
        self.progressbar = tqdm(
            desc=f'Downloading', 
            total=self.stream.filesize,
            ascii='░▓█',
            unit="Bytes", 
            unit_scale=True,
            unit_divisor=1024,
            ncols=int(self.config.TQDM_WIDTH)
        )
        self.stream.download(path)
        self.progressbar.close()
    
    def save_all(self, videos, path):
        for index, video in enumerate(videos):
            self.stream = self.get_stream(video, self.resolution)
            self.progressbar = tqdm(
                desc=f'{index + 1} of {self.total_videos}', 
                total=self.stream.filesize, 
                unit="Bytes", 
                unit_scale=True,
                ascii='░▓█',
                unit_divisor=1024,
                ncols=int(self.config.TQDM_WIDTH)
            )
            video.register_on_progress_callback(self.updateProgress)
            self.stream.download(path)
            self.progressbar.close()