def make_album(artist_name, album_title, number_of_songs=None):
    album={'artist' : artist_name, 'album' : album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album
while True:
    print("\nPlease tell me artist name: ")
    print("(enter 'q' at any time to quit)")
    a_name=input("Artist name: ")
    if a_name == 'q':
        break
    al_name=input("Album name: ")
    if al_name == 'q':
        break
    album_artist_name = make_album(a_name, al_name)
    print(f"\n{album_artist_name}")