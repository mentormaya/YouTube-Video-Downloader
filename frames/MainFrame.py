from tkinter import *

from frames.Header import Header


class MainFrame(Frame):
    def __init__(self, config, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.app_config = config
        self.title = f"Welcome to {self.app_config.APP_NAME}"
        self.status = StringVar()
        self.drawUI()
    
    def drawUI(self):
        mainContainer = Frame(self, bg=self.app_config.MAIN_BG_COLOR)
        
        self.header = Header(text=self.title, config=self.app_config, master=mainContainer)
        self.header.pack()
        
        mainContainer.pack(expand=True, fill=BOTH)