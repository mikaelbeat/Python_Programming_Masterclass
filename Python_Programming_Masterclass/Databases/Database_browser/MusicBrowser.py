
import sqlite3
import tkinter

conn = sqlite3.connect("music.sqlite")


class Scrollbox(tkinter.Listbox):
    
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)
        
    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
        self["yscrollcommand"] = self.scrollbar.set


def get_albums(event):
    lb = event.widget
    index = lb.curselection()[0]
    artist_name = lb.get(index),
    
    artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
    alist = []
    for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist=? ORDER BY albums.name", artist_id):
        alist.append(row[0])
    albumsLV.set(tuple(alist))

# MAIN WINDOWS

mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry("1024x768")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1) # Spacer column on right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# LABELS

tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# LISTS

artistsList = Scrollbox(mainWindow)
artistsList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30,0))
artistsList.config(border=2, relief="sunken")

for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    artistsList.insert(tkinter.END, artist[0])
    
artistsList.bind("<<ListboxSelect>>", get_albums)

albumsLV = tkinter.Variable(mainWindow)
albumsLV.set(("Choose artist",))
albumsList = Scrollbox(mainWindow, listvariable=albumsLV)
albumsList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
albumsList.config(border=2, relief="sunken")


songsLV = tkinter.Variable(mainWindow)
songsLV.set(("Choose album",))
songsList = Scrollbox(mainWindow, listvariable=songsLV)
songsList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
songsList.config(border=2, relief="sunken")

# MAIN LOOP

mainWindow.mainloop()
print("Closing database connection...")
conn.close()