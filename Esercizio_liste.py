playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]
playlist.append("Imagine")
playlist.append("Smells Like Teen Spirit")
playlist.insert(1, "Sweet Child O' Mine")
playlist[0] = "Hey Jude"
playlist.remove("Hotel California") 
playlist.pop(1)

print(len(playlist))
print(playlist)
