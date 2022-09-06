from telnetlib import AUTHENTICATION
from tkinter import *
from tqdm.auto import tqdm
from PIL import Image, ImageTk

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
        headerLabel.pack(padx=10, pady=5, side=TOP)
        
        contentContainer = Frame(
            master=mainContainer,
            bg=self.app_config.MAIN_BG_COLOR
        )
        contentContainer.pack(expand=True, fill=BOTH, side=TOP)
        
        contentContainer.columnconfigure(index=0, weight=1)
        contentContainer.columnconfigure(index=1, weight=5)
        contentContainer.columnconfigure(index=2, weight=5)
        contentContainer.columnconfigure(index=3, weight=1)
        
        author_img = Image.open(self.app_config.AUTHOR_IMG)
        author_img = author_img.resize((int(self.app_config.AUTHOR_IMG_SIZE), int(self.app_config.AUTHOR_IMG_SIZE)), Image.Resampling.LANCZOS)
        author_image = ImageTk.PhotoImage(author_img)
        
        imageLabel = Label(
            master=contentContainer,
            image=author_image,
            bg=self.app_config.MAIN_BG_COLOR
        )
        imageLabel.image = author_image
        imageLabel.pack(padx=10, pady=5, expand=True, fill=X)
        
        about_text = open(file='assets/contents/about.txt')
        
        about_label = Text(
            master=contentContainer,
            highlightthickness=self.app_config.CONSOLE_BORDER_THICKNESS,
            selectborderwidth=self.app_config.CONSOLE_BORDER_THICKNESS,
            highlightbackground=self.app_config.CONSOLE_BORDER_COLOR,
            bg=self.app_config.MAIN_BG_COLOR,
            fg=self.app_config.DISABLED_TEXT_COLOR,
            height=self.app_config.ABOUT_HEIGHT,
            font=(self.app_config.CONSOLE_FONT, self.app_config.CONSOLE_FONT_SIZE),
            insertbackground = 'white',
            padx=10,
            pady=10,
            spacing1 = 1,
            spacing3 = 1,
            wrap=WORD
        )
        about_label.insert(END, about_text.read())
        about_label.config(state=DISABLED)
        about_label.pack(padx=20, ipadx=10, ipady=10, side=BOTTOM, expand=True, fill=BOTH)
        
        mainContainer.pack(expand=True, fill=BOTH)
        self.status.updateStatus('AboutFrame Loaded!')