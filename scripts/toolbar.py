import tkinter as tk

def create_toolbar(win):
    toolbar=tk.Canvas(win, bg='#515151')
    close = tk.Button
    toolbar.place(relheight=0.05, relwidth=0.25, relx=0,rely=0)