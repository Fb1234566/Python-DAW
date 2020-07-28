import tkinter as tk
import tkinter.dnd as dnd
import browser
import toolbar
t=False
def cerate_track(playlist, number, name, t=True):
    if t:
        full_track=tk.Canvas(playlist,bg='white')
        track_info=tk.Canvas(full_track,bg='#515151')
        track_name=tk.Label(track_info,text=name, bg='#515151', fg='white')
        track_mute=tk.Button(track_info, text='M')
        track_solo=tk.Button(track_info, text='S')
        track_volume=tk.Scale(track_info,from_=200, to=0,bg='#515151',fg='white')
        track_volume.place(relx=0.45, rely=0.05,relheight=0.85)
        track_solo.place(relx=0.25, rely=0.45,relheight=0.25, relwidth=0.19)
        track_mute.place(relx=0.05, rely=0.45,relheight=0.25, relwidth=0.19)
        track_info.place(relwidth=0.15,relheight=1)
        track_name.place(relx=0.05, rely=0.15)
        full_track.place(relheight=0.125, relwidth=0.99,relx=0.005, rely=0.0085+(0.0085+0.125)*number)
def create_playlist(win,tracks=[['nome1'],['nome2'],['nome3'],['nome4']]):
    playlist_frame=tk.Frame(win)
    win.update_idletasks()
    final_x=(0.0085+(0.0085+0.125)*len(tracks))*(win.winfo_width()*0.75)
    playlist=tk.Canvas(playlist_frame,bg='grey',scrollregion=(0, 0, 1000, int(final_x)))
    for i in range(len(tracks)):
        cerate_track(playlist, i, tracks[i])
    playlist.place(relheight=1, relwidth=1)
    playlist_frame.place(relheight=0.85, relwidth=0.85, relx=0.15, rely=0.15)  