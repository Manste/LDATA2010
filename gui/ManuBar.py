from tkinter import *

class MenuBar(Menu):

    def __init__(self, ws):
        Menu.__init__(self, ws)
        file = Menu(self, tearoff=False)
        file.add_command(label="New")
        file.add_command(label="Open")
        file.add_command(label="Save")
        file.add_command(label="Save as")
        file.add_separator()
        file.add_command(label="Exit", underline=1, command=self.quit())
        self.add_cascade(label="File", underline=0, menu=file)

        view = Menu(self, tearoff=False)
        view.add_command(label="Full Screen")
        zoom_in = Menu(self, tearoff=False)
        for aspect_ratio in ('50:50', '75:75'):
            zoom_in.add_command(label=aspect_ratio)
        zoom_out = Menu(self, tearoff=False)
        for aspect_ratio in ('150:150', '175:175'):
            zoom_out.add_command(label=aspect_ratio)
        view.add_cascade(label="Zoom-in", menu=zoom_in)
        view.add_cascade(label="Zoom-out", menu=zoom_out)
        self.add_cascade(label='View', menu=view)

        window = Menu(self, tearoff = False)
        self.add_cascade(label='Window', menu=window)

        help = Menu(self, tearoff = False)
        help.add_command(label="About", command=self.about)
        self.add_cascade(label="Help", menu=help)

    def exit(self):
        self.exit

    def about(self):
        print('PythonGuides ', 'Python Guides aims at providing best practical tutorials')