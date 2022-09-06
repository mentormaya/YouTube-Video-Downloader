import sys
from tqdm.auto import tqdm

from tkinter import *
from tkinter import filedialog
from tkmacosx import Button as MacButton

from frames.Header import Header
from frames.Console import Console

from libs.YouTube import GetInfo, Download


class MainFrame(Frame):
    def __init__(self, config, status, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.app_config = config
        self.status = status
        self.get = False
        self.title = f"{self.app_config.APP_NAME}"
        self.subtitle = f'{self.app_config.APP_VERSION} coded with ❤️ by {self.app_config.AUTHOR}'
        self.playlist_ckeck = IntVar()
        self.path_to_save = self.app_config.OUTPUT_FOLDER
        self.drawUI()
    
    def drawUI(self):
        mainContainer = Frame(
            master=self,
            bg=self.app_config.MAIN_BG_COLOR
        )
        
        self.header = Header(
            text=[self.title, self.subtitle],
            image='./assets/images/YouTube-icon.png',
            config=self.app_config, 
            master=mainContainer,
            bg=self.app_config.MAIN_BG_COLOR
        )
        self.header.pack()
        
        self.inputContainer = LabelFrame(
            master=mainContainer,
            text='Provide the details:',
            bg=self.app_config.MAIN_BG_COLOR,
            fg=self.app_config.DISABLED_TEXT_COLOR,
        )
        
        self.inputContainer.columnconfigure(index=0, weight=1)
        self.inputContainer.columnconfigure(index=1, weight=2)
        self.inputContainer.columnconfigure(index=1, weight=2)
        self.inputContainer.columnconfigure(index=1, weight=2)
        
        url_label = Label(
            master=self.inputContainer,
            text='YouTube URL:',
            bg=self.app_config.MAIN_BG_COLOR,
            fg=self.app_config.DISABLED_TEXT_COLOR,
        )
        url_label.grid(row=0, column=0)
        
        url_input_validation = self.register(self.inputUpdated)
        
        self.url_input = Entry(
            master=self.inputContainer,
            font=('Times', 12, 'italic'),
            bg='white',
            fg=self.app_config.DISABLED_TEXT_COLOR,
            highlightthickness=0,
            validate="key", 
            validatecommand=(url_input_validation, '%P')
        )
        self.url_input.grid(row=0, column=1, columnspan=3, sticky=EW, padx=10)
        
        self.playlist_checkbox = Checkbutton(
            master=self.inputContainer,
            text='Want to download whole Playlist?',
            bg=self.app_config.MAIN_BG_COLOR,
            fg=self.app_config.DISABLED_TEXT_COLOR,
        )
        self.playlist_checkbox.select()
        
        self.file_browserLabel = Label(
            master=self.inputContainer,
            bg=self.app_config.MAIN_BG_COLOR,
            fg=self.app_config.DISABLED_TEXT_COLOR,
            text=f'Download will be saved to:{self.path_to_save}'
        )
        self.file_browserLabel.grid(row=2, column=0, columnspan=2, sticky=E)
        
        self.download_btn = MacButton(
            text ="Get Details", 
            command = self.get_info, 
            master = self.inputContainer,
            cursor='hand2',
            width=200,
            height=40,
            relief=GROOVE,
            borderless=1,
            bg=self.app_config.PRIMARY_COLOR,
            fg=self.app_config.PRIMARY_TEXT_COLOR,
            disabledforeground=self.app_config.DISABLED_TEXT_COLOR,
            disabledbackground=self.app_config.DISABLED_BG_COLOR,
            activebackground = self.app_config.PRIMARY_COLOR_ACTIVE,
            overbackground = self.app_config.SECONDARY_COLOR
        )
        self.cancel_btn = MacButton(
            text ="Clear", 
            command = self.clear_download, 
            master = self.inputContainer,
            cursor='hand2',
            width=200,
            height=40,
            relief=GROOVE,
            borderless=1,
            bg=self.app_config.PRIMARY_COLOR,
            fg=self.app_config.PRIMARY_TEXT_COLOR,
            disabledforeground=self.app_config.DISABLED_TEXT_COLOR,
            disabledbackground=self.app_config.DISABLED_BG_COLOR,
            activebackground = self.app_config.PRIMARY_COLOR_ACTIVE,
            overbackground = self.app_config.SECONDARY_COLOR
        )
        self.file_browser_btn = MacButton(
            text ="Browse", 
            command = self.setDownloadPath, 
            master = self.inputContainer,
            cursor='hand2',
            width=150,
            height=40,
            relief=GROOVE,
            borderless=1,
            bg=self.app_config.PRIMARY_COLOR,
            fg=self.app_config.PRIMARY_TEXT_COLOR,
            disabledforeground=self.app_config.DISABLED_TEXT_COLOR,
            disabledbackground=self.app_config.DISABLED_BG_COLOR,
            activebackground = self.app_config.PRIMARY_COLOR_ACTIVE,
            overbackground = self.app_config.SECONDARY_COLOR
        )
        
        self.file_browser_btn.grid(row=2, column=2, columnspan=2, padx=10, pady=5)
        self.cancel_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.download_btn.grid(row=3, column=2, columnspan=2, padx=10, pady=5)
        
        self.inputContainer.pack(padx=60, pady=10, expand=True, fill=X)
        
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
        sys.stderr = self.console
        
        self.console_text.pack(pady=10, padx=10, ipadx=10, ipady=10, side=BOTTOM, expand=True, fill=BOTH)
        
        mainContainer.pack(expand=True, fill=BOTH)
        
        self.status.updateStatus('MainFrame Loaded!')
    
    def inputUpdated(self, value=''):
        if (self.url_input.get() != '') and ('youtube.com/playlist' in self.url_input.get().lower()):
            self.playlist_checkbox.grid(row=1, column=1, columnspan=3, sticky=W, pady=5)
        else:
            self.playlist_checkbox.grid_forget()
        return True
    
    def setDownloadPath(self):
        path = filedialog.askdirectory(initialdir=self.path_to_save)
        if self.path_to_save is not None:
            self.path_to_save = path
            self.file_browserLabel.config(text=f'Downloads saved to: {self.path_to_save}')
            print(f'Downloads saved to: {self.path_to_save}')
    
    def clear_download(self):
        if self.get:
            self.download_btn.config(state=NORMAL, text="Get Info", command=self.get_info)
        print('Clearing downloads')
        self.url_input.delete(0, END)
    
    def get_info(self):
        url = self.url_input.get()
        if not url:
            # print("URL: ",url)
            print("Please Enter Your URL to proceed!")
            return
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
            downlod_thread = Download(self.yt, out_path=self.path_to_save)
            downlod_thread.daemon = True    ## auto clear the thread once the main app is terminated
            downlod_thread.start()
            self.check_download_complete(downlod_thread)

    def check_download_complete(self, thread):
        if thread.is_alive():
            self.after(500, lambda: self.check_download_complete(thread))
        else:
            self.download_btn.config(state=NORMAL, text="Get Info", command=self.get_info)
            self.status.updateStatus(f"Downloaded: {self.yt.title}!")
            self.get = False
            return True
        
    def check_info_complete(self, thread):
        if thread.is_alive():
            self.after(500, lambda: self.check_info_complete(thread))
        else:
            self.download_btn.config(state=NORMAL, text="Download", command=self.download)
            self.status.updateStatus("Details Fetched!")
            self.yt = thread.info
            self.get = True
            return True