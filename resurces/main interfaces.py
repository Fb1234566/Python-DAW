from tkinter import *
from tkinter.ttk import *

main_win=Tk()
main_win.geometry('1000x1000')
def Toolbar(window):
    def file_button_command():
        pass
    file_Button=Button(window)
    winx, winy=main_win.winfo_height(), main_win.winfo_width()
    print(winx,',',winy)
    file_Button.pack()

Toolbar(main_win)
main_win.mainloop()