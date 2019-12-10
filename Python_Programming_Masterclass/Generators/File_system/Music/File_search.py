import os, fnmatch


def find_albums(folder, artist_name):
    for path, directories, files in os.walk(folder):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album
                    
def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song
            
album_list = find_albums("Data", "Black Crowes")
song_list = find_songs(album_list)

for x in song_list:
    print(x)