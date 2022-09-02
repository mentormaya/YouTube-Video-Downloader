from tkinter import *

from frames.Header import Header

from libs.YouTube import GetInfo, Download


class MainFrame(Frame):
    def __init__(self, config, status, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.app_config = config
        self.status = status
        self.title = f"Welcome to {self.app_config.APP_NAME}"
        self.drawUI()
    
    def drawUI(self):
        mainContainer = Frame(self, bg=self.app_config.MAIN_BG_COLOR)
        
        self.header = Header(text=self.title, config=self.app_config, master=mainContainer)
        self.header.pack()
        
        self.download_btn = Button(
            text ="Get Details", 
            command = self.get_info, 
            master = mainContainer,
            cursor='hand2'
        )
        self.download_btn.pack(padx=10, pady=10)
        
        mainContainer.pack(expand=True, fill=BOTH)
        self.status.updateStatus('MainFrame Loaded!')
    
    def get_info(self):
        url = "https://www.youtube.com/watch?v=I2PsRRgRKto"
        purl = "https://www.youtube.com/playlist?list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-"
        self.download_btn.config(state=DISABLED)
        self.status.updateStatus("Fetching Details...")
        info_thread = GetInfo(purl, self.status)
        info_thread.daemon = True        ## auto clear the thread once the main app is terminated
        info_thread.start()
        self.check_info_complete(info_thread)
    
    def download(self):
        if self.yt is None:
            self.main_window.after(500, lambda: self.download())
        else:
            self.download_btn.config(state=DISABLED)
            self.status.updateStatus(f"Downloading {self.yt.title}...")
            downlod_thread = Download(self.yt)
            downlod_thread.daemon = True    ## auto clear the thread once the main app is terminated
            downlod_thread.start()
            self.check_download_complete(downlod_thread)

    def check_download_complete(self, thread):
        if thread.is_alive():
            self.after(500, lambda: self.check_download_complete(thread))
        else:
            self.download_btn.config(state=NORMAL, text="Get Info", command=self.get_info)
            self.status.updateStatus(f"Downloaded: {self.yt.title}!")
            return True
        
    def check_info_complete(self, thread):
        if thread.is_alive():
            self.after(500, lambda: self.check_info_complete(thread))
        else:
            self.download_btn.config(state=NORMAL, text="Download", command=self.download)
            self.status.updateStatus("Details Fetched!")
            self.yt = thread.info
            return True