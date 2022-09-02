from tkinter import *
from tkinter.ttk import Separator
from PIL import Image, ImageTk

class Header(Frame):
    def __init__(self, text, config, *args, **kwargs):
        super(Header, self).__init__(*args, **kwargs)
        self.app_config = config
        self.text = text
        self.drawUI()
    
    def drawUI(self):
        logo = Image.open('./assets/images/YouTube-icon.png')
        logo = logo.resize((75, 75), Image.ANTIALIAS)
        
        logoImage = ImageTk.PhotoImage(logo)
        
        imageLabel = Label(
            master=self,
            image=logoImage,
            bg=self.app_config.MAIN_BG_COLOR
        )
        imageLabel.image = logoImage
        imageLabel.pack(padx=10, pady=10, side=LEFT, expand=True)
        
        headerLabel = Label(
            master = self, 
            bg=self.app_config.MAIN_BG_COLOR,
            text = self.text,
            font = ("Monaco", 16, "bold")
        )
        headerLabel.pack(side=LEFT)
        
        seperator = Separator(self, orient='horizontal')
        seperator.pack(fill=X)
        