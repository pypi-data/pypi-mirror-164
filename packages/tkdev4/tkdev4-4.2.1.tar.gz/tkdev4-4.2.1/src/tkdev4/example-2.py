from tkdev4 import DevStack, DevWindow, DevManage
from darkdetect import isDark, isLight
from tkinter import *
from tkinter import ttk
from sv_ttk import use_light_theme, use_dark_theme


Window = DevWindow()
Window.title("MainWindow")
Manage = DevManage(Window)
Manage.add_window_sysmenu()


def auto():
    if isLight():
        Manage.dwm_set_window_attribute_use_light_mode()
        use_light_theme()
    elif isDark():
        Manage.dwm_set_window_attribute_use_dark_mode()
        use_dark_theme()


def light():
    Manage.dwm_set_window_attribute_use_light_mode()
    use_light_theme()


def dark():
    Manage.dwm_set_window_attribute_use_dark_mode()
    use_dark_theme()


def round():
    Manage.dwm_set_window_round_round()


def settings():
    Stack.show_page(2)


def back():
    Stack.show_page(1)


auto()
Stack = DevStack()

StartPage = ttk.Frame(Stack)
StartLogo = ttk.Label(StartPage, text="MainWindow Demo", font=("微软雅黑", 14), anchor="center")
StartLogo.pack(fill="both", expand="yes")
Stack.after(2000, lambda: Stack.show_page(1))

MainPage = ttk.Frame(Stack)
MainPage_Label = ttk.Label(MainPage, text="MainPage", font=("微软雅黑", 10), anchor="center")
MainPage_Label.pack(fill="both", expand="yes")
LeftBar_Setting = ttk.Button(MainPage, text="Settings", command=settings)
LeftBar_Setting.pack(fill="x", side="left", expand="yes")

SettingPage = ttk.Frame(Stack)

SettingTheme = ttk.Labelframe(SettingPage, text="Theme")
ThemeVar = StringVar()
ThemeVar.set("Auto")
AutoTheme = ttk.Radiobutton(SettingTheme, text="Auto", variable=ThemeVar, value="Auto", command=auto)
AutoTheme.pack(side="left", padx=10, pady=10)
LightTheme = ttk.Radiobutton(SettingTheme, text="Light", variable=ThemeVar, value="Light", command=light)
LightTheme.pack(side="left", padx=10, pady=10)
DarkTheme = ttk.Radiobutton(SettingTheme, text="Dark", variable=ThemeVar, value="Dark", command=dark)
DarkTheme.pack(side="left", padx=10, pady=10)
BackButton = ttk.Button(SettingTheme, text="Back", command=back)
BackButton.pack(side="right", anchor="e", padx=10, pady=10, ipadx=10)
SettingTheme.pack(fill="x", side="top", padx=10, pady=10)

SettingRound = ttk.Labelframe(SettingPage, text="Round")
RoundVar = StringVar()
RoundVar.set("Round")
Round = ttk.Radiobutton(SettingRound, text="Round", variable=RoundVar, value="Round", command=round)
Round.pack(side="left", padx=10, pady=10)
RoundSmall = ttk.Radiobutton(SettingRound, text="Round Small", variable=RoundVar, value="Round Small", command=light)
RoundSmall.pack(side="left", padx=10, pady=10)
DonotRound = ttk.Radiobutton(SettingRound, text="Donot Round", variable=RoundVar, value="Donot Round", command=dark)
DonotRound.pack(side="left", padx=10, pady=10)
BackButton2 = ttk.Button(SettingRound, text="Back", command=back)
BackButton2.pack(side="right", anchor="e", padx=10, pady=10, ipadx=10)
SettingRound.pack(fill="x", side="top", padx=10, pady=10)

Stack.add_page(StartPage, 0)
Stack.add_page(MainPage, 1)
Stack.add_page(SettingPage, 2)
Stack.show_page(0)
Stack.pack(fill="both", expand="yes")
Window.mainloop()