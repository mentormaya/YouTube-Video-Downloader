from datetime import datetime as dt
from turtle import bgcolor
from nepali_datetime import datetime as ndt
from tkinter import *
from tqdm.auto import tqdm
from tkinter.ttk import Separator

FONT_SIZE = 12

class StatusBar(Frame):
    def __init__(self, config, *args, **kwargs):
        super(StatusBar, self).__init__(*args, **kwargs)
        self.app_config = config
        self.copyright = f"ⒸCopyright {dt.now().year} reserved by {config.AUTHOR}"
        self.status = StringVar()
        self.status.set('Ready!')
        self.datetime = StringVar()
        self.updateTime()
        self.drawUI()
    
    def drawUI(self):
        statusFrame = Frame(
            master = self,
            height=self.master.winfo_height(),
            bg=self.app_config.STATUS_BAR_BG_COLOR
        )
        
        statusFrame.pack(expand=True, fill=BOTH)
        
        seperator = Separator(statusFrame, orient='horizontal')
        seperator.pack(expand=True, fill=X)
        
        self.statusBar = Frame(
            statusFrame,
            cursor='hand2',
            bg=self.app_config.STATUS_BAR_BG_COLOR
        )
        self.statusBar.columnconfigure(index=0, weight=4)
        self.statusBar.columnconfigure(index=1, weight=3)
        self.statusBar.columnconfigure(index=2, weight=2)
        
        self.statusLabel = Label(
            master = self.statusBar,
            textvariable = self.status,
            font = (self.app_config.URL_FONT, FONT_SIZE, "italic"),
            bg=self.app_config.STATUS_BAR_BG_COLOR,
            fg=self.app_config.STATUS_BAR_FG_COLOR,
            anchor=W
        )
        self.statusLabel.grid(row=0, column=0, sticky=SW)
        
        self.timeLabel = Label(
            master = self.statusBar, 
            textvariable = self.datetime,
            font = (self.app_config.SYSTEM_FONT, FONT_SIZE), 
            bg=self.app_config.STATUS_BAR_BG_COLOR,
            fg=self.app_config.STATUS_BAR_FG_COLOR
        )
        self.timeLabel.grid(row=0, column=2, sticky=S)
        
        self.copyrightLabel = Label(
            master = self.statusBar, 
            text = self.copyright,
            font = (self.app_config.URL_FONT, FONT_SIZE, "italic"), 
            bg=self.app_config.STATUS_BAR_BG_COLOR,
            fg=self.app_config.STATUS_BAR_FG_COLOR
        )
        self.copyrightLabel.grid(row=0, column=1, sticky=SE)
                
        self.statusBar.pack(padx=10, expand=True, fill=X, side=BOTTOM)
        self.setWidth()
    
    def setWidth(self):
        if 'App initialized!' not in self.status.get():
            print('App not initialized yet!')
            self.after(self.app_config.TIME_UPDATE_INTERVAL, self.setWidth)
        else:
            status_width = (self.statusBar.winfo_width() - self.timeLabel.winfo_width() - self.copyrightLabel.winfo_width()) // 10
            # print(f'setting width: {status_width}')
            self.statusLabel.config(width=status_width)
    
    def updateTime(self):
        self.datetime.set(ndt.now().strftime("%d %b, %Y %I:%M:%S %p"))
        self.after(self.app_config.TIME_UPDATE_INTERVAL, self.updateTime)
        
    def updateStatus(self, status):
        print(f'{status}')
        self.status.set(status)