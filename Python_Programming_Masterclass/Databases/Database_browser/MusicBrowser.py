
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

albumsList = tkinter.Variable(mainWindow)
albumsList.set(("Choose artist",))
albumsList = tkinter.Listbox(mainWindow, listvariable=albumsList)
albumsList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
albumsList.config(border=2, relief="sunken")

songsList = tkinter.Variable(mainWindow)
songsList.set(("Choose album",))
songsList = tkinter.Listbox(mainWindow, listvariable=songsList)
songsList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
songsList.config(border=2, relief="sunken")

# MAIN LOOP

mainWindow.mainloop()
print("Closing database connection...")
conn.close()