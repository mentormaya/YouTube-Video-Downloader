from tkinter.ttk import Frame, Label

from frames.Header import Header


class MainFrame(Frame):
    def __init__(self, master, config):
        super().__init__()
        self.master = master
        self.app_config = config
        self.title = f"Welcome to {self.app_config.APP_NAME}"
        self.drawUI()
    
    def drawUI(self):
        headerLabel = Header(self, self.title, self.app_config)
        headerLabel.pack(padx=10, pady=10)