from tkinter import *
from gui.ManuBar import MenuBar

app = Tk()

welcome_msg = Label(app, text="Welcome to Interaction Visualization Dashboard")

app.title("InfoVis")
#mainapp.minsize(640, 480)

width = app.winfo_screenwidth()
height = app.winfo_screenheight()
window_x = 800
window_y = 600
position_x = width // 2 - window_x // 2
position_y = height // 2 - window_y // 2

geo = "{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)

app.geometry(geo)

welcome_msg.pack()

# The menubar configuration
menubar = MenuBar(app)
app.config(menu=menubar)

app.mainloop()

