
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
        
        
class DataListBox(Scrollbox):
    
    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)
        
        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        
        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field
            
            
    def clear(self):
        self.delete(0, tkinter.END)
        
    def requery(self, link_value=None):
        if link_value:
            sql = self.sql_select + " WHERE " + " artist " + "=?" + self.sql_sort
            print(sql)
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)
            self.cursor.execute(self.sql_select + self.sql_sort)
        
        # Clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])


    def on_select(self, event):
        print(self is event.widget)
        index = self.curselection()[0]
        value = self.get(index),
    
        # get the artist ID from the database row
        link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + "=?", value).fetchone()[1]
        albumsList.requery(link_id)
        
    #     artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
    #     alist = []
    #     for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name", artist_id):
    #         alist.append(row[0])
    #     albumsLV.set(tuple(alist))
    #     songsLV.set(("Choose an album",))
    
def get_songs(event):
    lb = event.widget
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    # get the artist ID from the database row
    album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
    alist = []
    for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", album_id):
        alist.append(x[0])
    songsLV.set(tuple(alist))
    

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

artistsList = DataListBox(mainWindow, conn, "artists", "name")
artistsList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30,0))
artistsList.config(border=2, relief="sunken")

artistsList.requery()
    
artistsList.bind("<<ListboxSelect>>", license)

albumsLV = tkinter.Variable(mainWindow)
albumsLV.set(("Choose artist",))
albumsList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
albumsList.requery(12)
albumsList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
albumsList.config(border=2, relief="sunken")

albumsList.bind("<<ListboxSelect>>", get_songs)


songsLV = tkinter.Variable(mainWindow)
songsLV.set(("Choose album",))
songsList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
songsList.requery()
songsList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
songsList.config(border=2, relief="sunken")

# MAIN LOOP

mainWindow.mainloop()
print("Closing database connection...")
conn.close()