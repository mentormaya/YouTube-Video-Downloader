import tkinter as tk
class Console(): # create file like object
    def __init__(self, textbox, draw = False): # pass reference to text widget
        self.textbox = textbox # keep ref
        self.progress = False
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
        cr_index = text.find('\r')
        if cr_index >= 0:    #This loops take care of '\r' carriage return
            if self.progress:
                self.textbox.delete(tk.INSERT + " linestart", tk.END)   #deletes the lastline
            self.textbox.insert(tk.END, "\n" + text) # write contents to end of the textbox
            self.progress = True
        else:
            self.textbox.insert(tk.END, text)   # write text to textbox
        self.textbox.see("end")    # could also scroll to end of textbox here to make sure always visible
        self.textbox.configure(state="disabled")  # make field readonly

    def flush(self): # needed for file like object
        pass