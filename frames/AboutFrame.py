from tkinter import *
from tqdm.auto import tqdm

from frames.Header import Header

class AboutFrame(Frame):
    def __init__(self, config, status, *args, **kwargs):
        super(AboutFrame, self).__init__(*args, **kwargs)
        self.app_config = config
        self.status = status
        self.title = f"{self.app_config.APP_NAME}"
        self.subtitle = f"About App and Developer"
        self.drawUI()
    
    def drawUI(self):
        mainContainer = Frame(self, bg=self.app_config.MAIN_BG_COLOR)
        
        headerLabel = Header(
            text=[self.title, self.subtitle],
            image='./assets/images/YouTube-icon.png',
            config=self.app_config, 
            master=mainContainer,
            bg=self.app_config.MAIN_BG_COLOR
        )
        headerLabel.pack(padx=10, pady=10)
        
        mainContainer.pack(expand=True, fill=BOTH)
        self.status.updateStatus('AboutFrame Loaded!')