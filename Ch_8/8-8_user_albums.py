# 8-8 User Albums
# Use code from exercise 8-7. 
# Create a loop that allows user to create his own albums. Print the 
# created dictionary once data is provided. 
# Remember to include a quit option.

def make_album(artist_name, album_name, num_of_songs = None):
    """Returns a dictionary output with album information."""
    album = {'artist': artist_name, 'album': album_name}

    if num_of_songs:
        album['songs'] = num_of_songs
    
    return album

while True:
    print("Create an album! (Type in 'quit' any time to exit)")
    q_artist = input("Provide arist name: ")
    if q_artist == 'quit' or q_artist == 'q':
        break

    q_album = input("Provide album title: ")
    if q_album == 'quit' or q_album == 'q':
        break

    created_album = make_album(q_artist, q_album)
    print("\nResult:", created_album)