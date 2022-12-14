from tkinter import *

mainWindow = Tk("First window")
mainWindow.minsize(width = 300, height = 100)
text = Label(master = mainWindow, text = "First window created by Tkinter Lib")
text.place(x = 50, y = 50)
mainWindow.mainloop()