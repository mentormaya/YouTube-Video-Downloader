from tkinter import *

from frames.Header import Header

class AboutFrame(Frame):
    def __init__(self, config, *args, **kwargs):
        super(AboutFrame, self).__init__(*args, **kwargs)
        self.app_config = config
        self.title = f"About App and Developer"
        self.drawUI()
    
    def drawUI(self):
        headerLabel = Header(self, self.title, self.app_config)
        headerLabel.pack(padx=10, pady=10)