from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import down
from dotenv import dotenv_values
import threading

#-----------------------------------------------
# local Library
#-----------------------------------------------
from libs.PythonJson import PythonJson as Pjson     #could be used from dotmap import DotMap
from libs.YouTube import GetInfo, Download

#-----------------------------------------------
# Loading UI files
#-----------------------------------------------
from frames.MainFrame import MainFrame
from frames.AboutFrame import AboutFrame

config = Pjson(dotenv_values(".env"))
class App():
    def __init__(self):
        self.main_window = Tk()
        self.config = config
        self.yt = None
        self.setup()
        self.main_window.mainloop()
    
    def setup(self):
        self.setupUI()
        self.center()
        self.main_window.bind("<Key>", self.handle_keypress)
        self.main_window.update_idletasks()
    
    def setupUI(self):
        self.main_window.geometry(self.config.APP_SIZE)
        self.main_window.attributes('-alpha', self.config.ALPHA)
        self.main_window.title(self.config.APP_NAME + " " + self.config.APP_VERSION)
        main_frame = MainFrame(self.main_window, self.config)
        main_frame.pack()
        about_frame = AboutFrame(self.main_window, self.config)
        # about_frame.pack()
    
    def get_info(self):
        url = "https://www.youtube.com/watch?v=I2PsRRgRKto"
        purl = "https://www.youtube.com/playlist?list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-"
        info_thread = GetInfo(purl)
        info_thread.daemon = True        ## auto clear the thread once the main app is terminated
        info_thread.start()
        self.check_thread(info_thread)
    
    def download(self):
        if self.yt is None:
            self.main_window.after(500, lambda: self.download())
        else:
            downlod_thread = Download(self.yt)
            downlod_thread.daemon = True    ## auto clear the thread once the main app is terminated
            downlod_thread.start()
        
    def check_thread(self, thread):
        if thread.is_alive():
            self.main_window.after(500, lambda: self.check_thread(thread))
        else:
            self.yt = thread.info
            return True
        
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
    
    def quitApp(self, confirmation = False):
        if confirmation:
            if not messagebox.askokcancel("Quit", "Do you want to exit?"):
                return
        self.main_window.destroy()

if __name__ == '__main__':
    app = App()