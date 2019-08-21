class Song:
    """ Class to represent a song
        Attributes
            - title
            - artist
            - duration
    """
    
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration
        
              
class Album:
    """ Class to represent a album
        Attributes
            - artist
            - album_name
            - tracks
            - year
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []
        
    def add_song(self, song, position=None):
        if position is None:
            self.tracksappend(song)
        else:
            self.tracks.insert(position, song)
            
            
class Artist:
    """ Class to represent artist
        Attributes
            - name
            - album
    """
    
    def __init__(self, name):
        self.name = name
        self.albums = []
        
    def add_album(self, album):
        self.albums.append(album)
        
        
def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    
    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)
            
            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None
                
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)
                
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)
            
        # 9:08
            
if __name__ == "__main__":
    load_data()
            

        
    
    