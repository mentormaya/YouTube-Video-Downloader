import platform
from tkinter import *
from tkinter import messagebox
from turtle import width
from dotenv import dotenv_values

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

config = Pjson(dotenv_values(".env"))
class App():
    def __init__(self):
        self.main_window = Tk()
        self.config = config
        self.config.OS = platform.system()
        self.yt = None
        self.setup()
        self.main_window.mainloop()
    
    def setup(self):
        self.content_height=self.main_window.winfo_height() - int(self.config.STATUS_BAR_HEIGHT), 
        self.content_width=self.main_window.winfo_width()
        if 'darwin' in self.config.OS.lower():
            self.main_window.iconbitmap('./assets/images/YouTube.icns')
        else:
            self.main_window.iconbitmap('./assets/images/YouTube.ico')
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
        
        self.statusBar = StatusBar(
            config=self.config, 
            master=self.main_window, 
            height=self.config.STATUS_BAR_HEIGHT,
            bg=self.config.STATUS_BAR_BG_COLOR
        )
        
        main_frame = MainFrame(
            config=self.config,
            status=self.statusBar,
            master=self.main_window, 
            height=self.content_height,
            width=self.content_width
        )
        main_frame.pack(expand=True, fill=BOTH)
        # main_frame.pack_propagate(False)
        # main_frame.grid(row=0, column=0)
        # about_frame = AboutFrame(self.main_window, self.config)
        # about_frame.pack()
        
        self.statusBar.pack_propagate(False)
        self.statusBar.pack(side=BOTTOM, fill=X)
        
        self.statusBar.updateStatus("App initialized!")
        
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