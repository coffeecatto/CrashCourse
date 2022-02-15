# 8-7 Album
# Create funciton make_album() that includes artist's name, album name and
# number of songs (optional - default value 'None'). 
# Information should be returned in a form of a dictionary. 
def make_album(artist_name, album_name, num_of_songs = None):
    """Returns a dictionary output with album information."""
    album = {'artist': artist_name, 'album': album_name}

    if num_of_songs:
        album['songs'] = num_of_songs
    
    return album

# Create three different dictionaries. 
album_1 = make_album('kavinsky', 'outrun')
album_2 = make_album('david bowie', 'low', 11)
album_3 = make_album('circle electro', 'sweet agony (ep)')

print(album_1)
print(album_2)
print(album_3)