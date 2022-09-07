import os, sys
import platform
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, st
from PIL import Image, ImageTk
from dotenv import dotenv_values
from tkmacosx import Button as MacButton

#-----------------------------------------------
# local Library
#-----------------------------------------------
from libs.PythonJson import PythonJson as Pjson     #could be used from dotmap import DotMap

#-----------------------------------------------
# Loading UI files
#-----------------------------------------------
from frames.MainFrame import MainFrame
from frames.AboutFrame import AboutFrame
from frames.StatusBar import StatusBar

extDataDir = os.getcwd()
if getattr(sys, 'frozen', False):
    extDataDir = sys._MEIPASS

config = Pjson(dotenv_values(os.path.join(extDataDir, '.env')))
class App():
    def __init__(self):
        self.main_window = Tk()
        self.config = config
        self.config.OS = platform.system()
        self.main_window.FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        self.main_window.extDataDir = extDataDir
        self.yt = None
        self.about = False
        self.setup()
        self.main_window.mainloop()
    
    def setup(self):
        self.content_height=self.main_window.winfo_height() - int(self.config.STATUS_BAR_HEIGHT), 
        self.content_width=self.main_window.winfo_width()
        photoIcon = PhotoImage(file = os.path.join(self.main_window.extDataDir, 'assets/images/YouTube-icon.png'))
        self.main_window.iconphoto(False, photoIcon)
        if 'darwin' in self.config.OS.lower():
            self.main_window.iconbitmap(os.path.join(self.main_window.extDataDir, 'assets/images/YouTube.icns'))
        else:
            self.main_window.iconbitmap(os.path.join(self.main_window.extDataDir, 'assets/images/YouTube.ico'))
        self.setupUI()
        self.center()
        self.main_window.bind("<Key>", self.handle_keypress)
        self.main_window.update_idletasks()
    
    def setupUI(self):
        self.main_window.geometry(self.config.APP_SIZE)
        if self.config.ALPHA:
            self.main_window.attributes('-alpha', self.config.ALPHA)
        self.main_window.title(self.config.APP_NAME + " " + self.config.APP_VERSION)
        self.main_window.config(bg=self.config.MAIN_BG_COLOR)
        
        self.contentFrame = Frame(
            master=self.main_window,
            bg=self.config.MAIN_BG_COLOR,
        )
        
        self.contentFrame.pack(expand=True, fill=X)
        
        self.statusBar = StatusBar(
            config=self.config, 
            master=self.main_window, 
            height=self.config.STATUS_BAR_HEIGHT,
            bg=self.config.STATUS_BAR_BG_COLOR
        )
        self.statusBar.pack(side=BOTTOM, fill=X)
        
        self.contentFrame.columnconfigure(index=0, weight=1)
        self.contentFrame.columnconfigure(index=1, weight=5)
        self.contentFrame.columnconfigure(index=2, weight=5)
        self.contentFrame.columnconfigure(index=3, weight=1)
        
        
        info_image = Image.open(os.path.join(self.main_window.extDataDir, 'assets/images/information-icon.png'))
        info_image = info_image.resize((int(self.config.INFO_BTN_DIMENSION), int(self.config.INFO_BTN_DIMENSION)), Image.Resampling.LANCZOS)
        info_photo = ImageTk.PhotoImage(info_image)
        
        self.infoBtn = MacButton(
            master=self.main_window, 
            image = info_photo, 
            fg=self.config.PRIMARY_TEXT_COLOR,
            bg=self.config.MAIN_BG_COLOR,
            overbackground = self.config.PRIMARY_COLOR,
            cursor='hand2', 
            command=self.showAbout
        )
        self.infoBtn.image = info_photo
        self.infoBtn.place(relx=1, rely=0, x = -2, y = 2, anchor=NE)
        self.main_window.after(200, lambda: self.infoBtn.lift())
        
        self.about_frame = AboutFrame(
            master=self.contentFrame, 
            config=self.config,
            status=self.statusBar
        )
        
        self.main_frame = MainFrame(
            config=self.config,
            status=self.statusBar,
            master=self.contentFrame, 
            height=self.content_height,
            width=self.content_width
        )
        self.main_frame.grid(row=0, column=0, columnspan=4, sticky=EW)
        self.main_frame.tkraise()
        self.statusBar.updateStatus("App initialized!")
    
    def showAbout(self):
        if self.about:
            # print('hiding about frame')
            self.about_frame.grid_forget()
            self.main_frame.grid(row=0, column=0, columnspan=4, sticky=EW)
            self.main_frame.tkraise()
            self.about = False
        else:
            # print('showing about frame')
            self.main_frame.grid_forget()
            self.about_frame.grid(row=0, column=0, columnspan=4, sticky=EW)
            self.about_frame.tkraise()
            self.about = True
    
    def center(self):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        self.main_window.update_idletasks()
        width = self.main_window.winfo_width()
        frm_width = self.main_window.winfo_rootx() - self.main_window.winfo_x()
        win_width = width + 2 * frm_width
        height = self.main_window.winfo_height()
        titlebar_height = self.main_window.winfo_rooty() - self.main_window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.main_window.winfo_screenwidth() // 2 - win_width // 2
        y = self.main_window.winfo_screenheight() // 2 - win_height // 2
        self.main_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.main_window.deiconify()
    
    def handle_keypress(self, event):
        if event.keysym == 'Escape':
            print('Escape Key Pressed: App Closing...')
            self.quitApp()
            return
        else:
            pass
            # print(event)
    
    def quitApp(self, confirmation = False):
        if confirmation:
            if not messagebox.askokcancel("Quit", "Do you want to exit?"):
                return
        self.main_window.destroy()

if __name__ == '__main__':
    app = App()