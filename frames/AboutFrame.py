from tkinter.ttk import Frame, Label

from frames.Header import Header

class AboutFrame(Frame):
    def __init__(self, master, config):
        super().__init__()
        self.master = master
        self.app_config = config
        self.title = f"About App and Developer"
        self.drawUI()
    
    def drawUI(self):
        headerLabel = Header(self, self.title, self.app_config)
        headerLabel.pack(padx=10, pady=10)