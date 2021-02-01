
from tkinter import *
from module.interface import *

# Create the window
window = Tk()
window.title("ECS Shopping Basket")
window.geometry("720x480")
window.minsize(720,480)
window.config(background='#dee5dc')
app = Interface(window)
window.mainloop()
