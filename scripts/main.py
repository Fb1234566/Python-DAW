from playlist import *
from toolbar import *
from browser import *
import tkinter as tk

#create interface
main_win = tk.Tk()
create_playlist(main_win)
create_browser(main_win)
create_toolbar(main_win)
