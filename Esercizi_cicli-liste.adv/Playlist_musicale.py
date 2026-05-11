# Hai una playlist di brani. Devi visualizzarla, ordinarla e cercare brani al suo interno. 
# Tutte le funzioni che scorrono la lista devono usare enumerate, non range(len(...)).

playlist = [
    "Bohemian Rhapsody", "Hotel California", "Stairway to Heaven",
    "Smells Like Teen Spirit", "Imagine", "Purple Rain",
    "Like a Rolling Stone", "Johnny B. Goode"
]

def stampa_playlist(playlist):
    for i, brano in enumerate(playlist, 1):
        print(i, brano)

stampa_playlist(playlist)

def ordina_playlist(playlist):
    playlist.sort()
    stampa_playlist(playlist)
print("*"*50)
ordina_playlist(playlist)


def playlist_ordinata_copia (playlist):
    playlist_ordinata = sorted(playlist)
    print(playlist_ordinata)

print("*"*50)
playlist_ordinata_copia(playlist)

def inverti_playlist(playlist):
    playlist.reverse()
    for i, brano in enumerate(playlist, 1):
        print(i, brano)

print("*"*50)
inverti_playlist(playlist)

def trova_posizione(playlist, titolo):
    for i, brano in enumerate(playlist, 1):
        if brano == titolo:
            return i
    return -1
print("*"*50)
print(trova_posizione(playlist, "Imagine"))

def brani_meta_finale(playlist):
    risultato= []
    for i, brano in enumerate(playlist):
        if i >= len(playlist)//2:
            risultato.append(brano)
    return risultato
print("*"*50)   
print(brani_meta_finale(playlist))
        
meta_playlist = playlist[len(playlist)//2:]
print("*"*50)  
print(meta_playlist)