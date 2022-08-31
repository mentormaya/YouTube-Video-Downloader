from tkinter import *
from tkinter.ttk import Separator
from datetime import datetime as dt

FONT_SIZE = 12

class StatusBar(Frame):
    def __init__(self, config, *args, **kwargs):
        super(StatusBar, self).__init__(*args, **kwargs)
        self.app_config = config
        self.copyright = f"ⒸCopyright {dt.now().year} reserved by {config.AUTHOR}"
        self.status = StringVar()
        self.status.set('Ready!')
        self.drawUI()
    
    def drawUI(self):
        self.statusBar = Frame(self, bg=self.app_config.STATUS_BAR_BG_COLOR)
        seperator = Separator(self.statusBar, orient='horizontal')
        seperator.pack(expand=True, fill=X)
        self.statusLabel = Label(
            master = self.statusBar,
            textvariable = self.status,
            font = ("Times", FONT_SIZE, "italic"), 
            bg=self.app_config.STATUS_BAR_BG_COLOR,
            fg=self.app_config.STATUS_BAR_FG_COLOR
        )
        self.statusLabel.pack(side=LEFT)
        self.copyrightLabel = Label(
            master = self.statusBar, 
            text = self.copyright,
            font = ("Times", FONT_SIZE, "italic"), 
            bg=self.app_config.STATUS_BAR_BG_COLOR,
            fg=self.app_config.STATUS_BAR_FG_COLOR
        )
        self.copyrightLabel.pack(side=RIGHT)
        self.timeLabel = Label(
            master = self.statusBar, 
            text = dt.now().strftime("%d %b, %Y %I:%M:%S"),
            font = ("Times", FONT_SIZE), 
            bg=self.app_config.STATUS_BAR_BG_COLOR,
            fg=self.app_config.STATUS_BAR_FG_COLOR
        )
        self.timeLabel.pack(side=RIGHT)
        self.statusBar.pack(expand=True, fill=X, side=BOTTOM)
    
    def updateStatus(self, status):
        print(f'{status}')
        self.status.set(status)
        