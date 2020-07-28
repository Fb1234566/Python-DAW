import tkinter as tk

def create_browser(win):
    browser= tk.Canvas(win, bg='#515151')
    prova=tk.Label(browser,text='prova')
    prova.pack()
    browser.place(relwidth=0.15, relheight=0.85, rely=0.15, relx=0)
    