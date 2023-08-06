from re import I
from tkdev4 import DevWindow, Icon_Folder
from tkfontawesome import icon_to_image



class Window(DevWindow):
    def __init__(self, title: str = "", size=(730, 540), icon=Icon_Folder):
        super().__init__(title=title, size=size, icon=icon)


if __name__ == "__main__":
    root = Window()
    root.mainloop()