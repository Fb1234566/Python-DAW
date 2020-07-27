import tkinter as tk
import numpy as np

#creating interface
def create_interface():
    main_win=tk.Tk()
    play=tk.Button(main_win, text='play')
    play.pack()
    main_win.mainloop()

create_interface()