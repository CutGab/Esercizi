while True:

    opzione = (input("Vuoi inserire un album?: (Y/N)").lower())
    
    if opzione == "n":
            break

    elif opzione == "y":

        music_album: dict = {}
            
        name = (input("Inserisci il nome dell'artista: "))

        music_album ["Nome"] = name
           
        album = (input("Inserisci il nome dell'album: "))

        music_album ["Album"] = album
        
def make_album(name: str, album: str):
    
    print(music_album)

    return music_album

make_album(name, album)
        
