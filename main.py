from tkinter import *
from tkinter import ttk
from dotenv import dotenv_values

#-----------------------------------------------
# local Library
#-----------------------------------------------
from libs.PythonJson import PythonJson as Pjson     #could be used from dotmap import DotMap
from libs.YouTube import Downloader

config = Pjson(dotenv_values(".env"))
class App():
    def __init__(self):
        self.main_window = Tk()
        self.config = config
        self.downloader = Downloader()
        self.setup()
        self.main_window.mainloop()
    
    def setup(self):
        self.setupUI()
        self.center()
        self.main_window.bind("<Key>", self.handle_keypress)
        self.download()
    
    def setupUI(self):
        self.main_window.geometry(self.config.APP_SIZE)
        self.main_window.attributes('-alpha', self.config.ALPHA)
        self.main_window.title(self.config.APP_NAME + " " + self.config.APP_VERSION)
        main_frame = ttk.Frame()
        main_frame.pack()
        ttk.Label(
            master=main_frame, 
            text=   "Welcome to YouTube Downloader",
            font=   ("Monaco", 20, "bold")
        ).pack(padx=10, pady=10)
    
    def download(self):
        url = "https://www.youtube.com/watch?v=I2PsRRgRKto"
        self.downloader.get()
        # self.downloader.download()
        
    
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
            print(event)
    
    def quitApp(self):
        self.main_window.destroy()

if __name__ == '__main__':
    app = App()