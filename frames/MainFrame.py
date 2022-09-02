import sys
from tkinter import *

from frames.Header import Header
from frames.Console import Console

from libs.YouTube import GetInfo, Download


class MainFrame(Frame):
    def __init__(self, config, status, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.app_config = config
        self.status = status
        self.title = f"Welcome to {self.app_config.APP_NAME}"
        self.drawUI()
    
    def drawUI(self):
        mainContainer = Frame(
            master=self,
            bg=self.app_config.MAIN_BG_COLOR
        )
        
        self.header = Header(
            text=self.title, 
            config=self.app_config, 
            master=mainContainer,
            bg=self.app_config.MAIN_BG_COLOR
        )
        self.header.pack()
        
        self.download_btn = Button(
            text ="Get Details", 
            command = self.get_info, 
            master = mainContainer,
            cursor='hand2',
            width=50,
            height=2,
            relief=GROOVE,
            fg=self.app_config.PRIMARY_TEXT_COLOR,
            disabledforeground=self.app_config.DISABLED_TEXT_COLOR,
            bg=self.app_config.PRIMARY_COLOR,
            activebackground = self.app_config.PRIMARY_COLOR_ACTIVE,
        )
        self.download_btn.pack(padx=10, pady=10)
        
        self.console_text = Text(
            master=mainContainer,
            highlightthickness=self.app_config.CONSOLE_BORDER_THICKNESS,
            selectborderwidth=self.app_config.CONSOLE_BORDER_THICKNESS,
            highlightbackground=self.app_config.CONSOLE_BORDER_COLOR,
            bg=self.app_config.CONSOLE_BACKGROUD_COLOR,
            fg=self.app_config.CONSOLE_TEXT_COLOR,
            height=self.app_config.CONSOLE_HEIGHT,
            font=(self.app_config.CONSOLE_FONT, self.app_config.CONSOLE_FONT_SIZE)
        )
        self.console = Console(self.console_text)
        # replace sys.stdout with our object
        sys.stdout = self.console
        self.console_text.pack(pady=10, padx=10, ipadx=10, ipady=10, side=BOTTOM, expand=True, fill=BOTH)
        
        mainContainer.pack(expand=True, fill=BOTH)
        
        self.status.updateStatus('MainFrame Loaded!')
    
    def get_info(self):
        url = "https://www.youtube.com/watch?v=I2PsRRgRKto"
        purl = "https://www.youtube.com/playlist?list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-"
        self.download_btn.config(state=DISABLED)
        self.status.updateStatus("Fetching Details...")
        info_thread = GetInfo(url, self.status)
        info_thread.daemon = True        ## auto clear the thread once the main app is terminated
        info_thread.start()
        self.check_info_complete(info_thread)
    
    def download(self):
        if self.yt is None:
            self.main_window.after(500, lambda: self.download())
        else:
            self.download_btn.config(state=DISABLED)
            # self.status.updateStatus(f"Downloading {self.yt.title}...")
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