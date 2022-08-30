from tkinter.ttk import Frame, Label, Separator


class Header(Frame):
    def __init__(self, master, text, config):
        super().__init__()
        self.master = master
        self.app_config = config
        self.text = text
        self.drawUI()
    
    def drawUI(self):
        headerLabel = Label(
            master = self, 
            text = self.text,
            font = ("Monaco", 20, "bold")
        )
        headerLabel.pack(padx=10, pady=10)
        
        seperator = Separator(self, orient='horizontal')
        seperator.pack(fill='x')
        