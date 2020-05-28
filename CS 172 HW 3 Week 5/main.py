import media

media_library = []
movie_library = []
song_library = []
picture_library = []

# base objects are just so I can call the add() method through them
baseMovie = media.Movie("no", 1, "no", 1)
baseSong = media.Song("no", 1, "no", "no")
basePicture = media.Picture("no", 1, 1)

def menu_op():
    print("\n*** Media Library ***")
    print("a. Display all Media")
    print("b. Display only Songs")
    print("c. Display only Movies")
    print("d. Display only Pictures")
    print("e. Play a Song")
    print("f. Play a Movie")
    print("g. Show a Picture")
    print("h. Add a Song")
    print("i. Add a Movie")
    print("j. Add a Picture")
    print("k. Exit the program")
    
    choice = input("\nEnter your choice: ")
    if choice.lower() == "a":
        for media in media_library:
            if type(media) == type(baseSong):
                print("Song: {}".format(media))
            if type(media) == type(baseMovie):
                print("Movie: {}".format(media))
            if type(media) == type(basePicture):
                print("Picture: {}".format(media))
        menu_op()
    
    if choice.lower() == "b":
        for media in song_library:
            print("Song: {}".format(media))
        menu_op()
        
    if choice.lower() == "c":
        for media in movie_library:
            print("Movie: {}".format(media))
        menu_op()
        
    if choice.lower() == "d":
        for media in picture_library:
            print("Picture: {}".format(media))
        menu_op()
    
    if choice.lower() == "e":
        toplay = input("Enter name of the song to play:")
        song_names = []
        for song in song_library:
            name = song.getName()
            song_names.append(name)
        if toplay in song_names:
            for song in song_library:
                if song.getName() == toplay:
                    print(song.play())
            menu_op()
        else :
            print("No such song in the media library")
            menu_op()
            
    if choice.lower() == "f":
        toplay = input("Enter name of the movie to play:")
        movie_names = []
        for movie in movie_library:
            name = movie.getName()
            movie_names.append(name)
        if toplay in movie_names:
            for movie in movie_library:
                if movie.getName() == toplay:
                    print(movie.play())
            menu_op()
        else :
            print("No such movie in the media library")
            menu_op()
    
    if choice.lower() == "g":
        toshow = input("Enter name of the picture to show:")
        picture_names = []
        for picture in picture_library:
            name = picture.getName()
            picture_names.append(name)
        if toshow in picture_names:
            for picture in picture_library:
                if picture.getName() == toshow:
                    print(picture.show())
            menu_op()
        else :
            print("No such picture in the media library")
            menu_op()
    
    if choice.lower() == "h":
        newSong = baseSong.add()
        media_library.append(newSong)
        song_library.append(newSong)
        menu_op()
        
    if choice.lower() == "i":
        newMovie = baseMovie.add()
        media_library.append(newMovie)
        movie_library.append(newMovie)
        menu_op()
        
    if choice.lower() == "j":
        newPicture = basePicture.add()
        media_library.append(newPicture)
        picture_library.append(newPicture)
        menu_op()
        
    if choice.lower() == "k":
        print("Good-Bye!")

if __name__ == "__main__":
    menu_op()
    