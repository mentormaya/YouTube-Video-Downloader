from tkinter import *
from tkinter.ttk import Separator


class Header(Frame):
    def __init__(self, text, config, *args, **kwargs):
        super(Header, self).__init__(*args, **kwargs)
        self.app_config = config
        self.text = text
        self.drawUI()
    
    def drawUI(self):
        imageLabel = Label(
            master=self,
            text='Logo',
            bg=self.app_config.MAIN_BG_COLOR
        ).pack()
        
        headerLabel = Label(
            master = self, 
            bg=self.app_config.MAIN_BG_COLOR,
            text = self.text,
            font = ("Monaco", 20, "bold")
        )
        headerLabel.pack()
        
        seperator = Separator(self, orient='horizontal')
        seperator.pack(fill=X)
        