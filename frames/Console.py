import tkinter as tk

class Console(): # create file like object
    def __init__(self, textbox, draw = False): # pass reference to text widget
        self.textbox = textbox # keep ref
        self.setup()
        if draw:
            self.drawConsole()
    
    def setup(self):
        self.textbox.config(
            insertbackground = 'white',
            padx=10,
            pady=10,
            spacing1 = 1,
            spacing3 = 1,
            wrap=tk.WORD
        )
    
    def drawConsole(self):
        self.textbox.config(
            bg='grey',
            fg='green'
        )

    def write(self, text):
        self.textbox.configure(state="normal")  # make field editable
        self.textbox.insert(tk.END, text) # write text to textbox
        self.textbox.see("end")    # could also scroll to end of textbox here to make sure always visible
        self.textbox.configure(state="disabled")  # make field readonly


    def flush(self): # needed for file like object
        pass