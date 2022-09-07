import os
from tkinter import *
from tqdm.auto import tqdm
from tkinter.ttk import Separator
from PIL import Image, ImageTk

class Header(Frame):
    def __init__(self, text, image, config, *args, **kwargs):
        super(Header, self).__init__(*args, **kwargs)
        self.app_config = config
        self.text = text
        self.image = image
        self.drawUI()
    
    def drawUI(self):
        logo = Image.open(os.path.join(self.master.master.master.master.extDataDir, self.image))
        logo = logo.resize((75, 75), Image.Resampling.LANCZOS)
        
        logoImage = ImageTk.PhotoImage(logo)
        
        imageLabel = Label(
            master=self,
            image=logoImage,
            bg=self.app_config.MAIN_BG_COLOR
        )
        imageLabel.image = logoImage
        imageLabel.pack(padx=10, pady=10, side=LEFT, expand=True)
        
        textContainer = Frame(
            master = self,
            bg=self.app_config.MAIN_BG_COLOR
        )
        textContainer.pack(side=LEFT)
        
        headerLabel = Label(
            master = textContainer, 
            bg=self.app_config.MAIN_BG_COLOR,
            fg=self.app_config.SECONDARY_COLOR,
            text = self.text[0],
            font=(self.app_config.SYSTEM_FONT, 16)
        )
        headerLabel.pack(side=TOP, expand=True, fill=X)
        
        versionLabel = Label(
            master = textContainer, 
            bg=self.app_config.MAIN_BG_COLOR,
            fg=self.app_config.SECONDARY_COLOR,
            text = self.text[1],
            font=(self.app_config.URL_FONT, 11, 'italic'),
            anchor=W,
            justify=LEFT,
        )
        versionLabel.pack(side=TOP, expand=True, fill=X)
        
        seperator = Separator(self, orient='horizontal')
        seperator.pack(fill=X)
        