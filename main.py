from libs.PythonJson import PythonJson as Pjson
from dotenv import dotenv_values
from tkinter import *

config = Pjson(dotenv_values(".env"))
class App():
    def __init__(self):
        self.app = Tk()
        self.config = config
        
    


if __name__ == '__main__':
    app = App()