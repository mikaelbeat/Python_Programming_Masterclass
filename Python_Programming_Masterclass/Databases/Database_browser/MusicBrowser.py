
import sqlite3
import tkinter

conn = sqlite3.connect("music.sqlite")

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

artistsList = tkinter.Listbox(mainWindow)
artistsList.grid(row=1, column=0, sticky="nsew", padx=(30,0))
artistsList.config(border=2, relief="sunken")

artistsScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistsList.yview)
artistsScroll.grid(row=1, column=0, sticky="nse", rowspan=2)
artistsList["yscrollcommand"] = artistsScroll.set

albumsList = tkinter.Variable(mainWindow)
albumsList.set(("Choose artist",))
albumsList = tkinter.Listbox(mainWindow, listvariable=albumsList)
albumsList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
albumsList.config(border=2, relief="sunken")

albumsScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumsList.yview)
albumsScroll.grid(row=1, column=1, sticky="nse", rowspan=2)
albumsScroll["yscrollcommand"] = albumsScroll.set

songsList = tkinter.Variable(mainWindow)
songsList.set(("Choose album",))
songsList = tkinter.Listbox(mainWindow, listvariable=songsList)
songsList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
songsList.config(border=2, relief="sunken")

# MAIN LOOP

testList = range(0, 100)
albumsList.set(tuple(testList))
mainWindow.mainloop()
print("Closing database connection...")
conn.close()