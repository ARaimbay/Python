def make_album(artist_name, album_title, number_of_songs=None):
    album={'artist' : artist_name, 'album' : album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album
first_album = make_album('blue', 'my blue nights', number_of_songs=8)
print(first_album)