import tkinter as tk

def create_playlist(win,tracks=[1,2,3,4,5,6,7,8,9]):
    playlist=tk.Canvas(win,bg='grey')
    def cerate_track(playlist, number):
        track=tk.Canvas(playlist,bg='white')
        print(number)
        track.place(relheight=0.125, relwidth=0.99,relx=0.005, rely=0.0085+(0.0085+0.125)*number)
    for i in range(len(tracks)):
        cerate_track(playlist, i)

    
    playlist.place(relheight=0.75, relwidth=0.75, relx=0.25, rely=0.25)
win=tk.Tk()
win.attributes('-fullscreen', True)
create_playlist(win)
tk.mainloop()