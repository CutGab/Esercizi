def make_album(name: str, album: str, number_songs = None):
    
    music_album:dict = {}

    music_album ["Nome"] = name

    music_album ["Nome Album"] = album

    if number_songs:
        music_album ["Numero Canzoni"] = number_songs

    return music_album

print (make_album("Vasco Rossi", "Siamo Soli", 10))

print (make_album("Kendrick Lamar", "The Heart"))

print (make_album("Tiziano Ferro", "Accetto Miracoli"))