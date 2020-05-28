from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, name: str, rating: int):
        self.name = name
        self.rating = rating
        
    def __str__(self):
        return "{} {}".format(self.name, self.rating)
    
    def getName(self):
        return self.name
    
    def getRating(self):
        return self.rating
    
    def setRating(self, value):
        self.rating = value
        
    @abstractmethod
    def add(self):
        pass
    
class Movie(Media):
    def __init__(self, name, rating, director, running_time):
        self.name = name
        self.rating = rating
        self.director = director
        self.running_time = running_time
    
    def getDirector(self):
        return self.director
    
    def setDirector(self, name):
        self.director = name
        
    def getRunningTime(self):
        return self.running_time
    
    def setRunningTime(self, time):
        self.running_time = time
        
    def play(self):
        return "{}, {} stars, Directed by: {}, Running time: {} minutes.".format(self.name, self.rating, self.director, self.running_time)
    
    def __str__(self):
        return self.play()
        
    def add(self):
        name = input("Enter movie name: ")
        director = input("Enter director: ")
        duration = int(input("Enter movie duration: "))
        rating = int(input("Enter rating: "))
        newMovie = Movie(name, rating, director, duration)
        print("Movie added!")
        return newMovie
    
class Song(Media):
    def __init__(self, name, rating, artist, album):
        self.name = name
        self.rating = rating
        self.artist = artist
        self.album = album
    
    def getArtist(self):
        return self.artist
    
    def setArtist(self, name):
        self.artist = name
        
    def getAlbum(self):
        return self.album
    
    def setAlbum(self, name):
        self.album = name
        
    def play(self):
        return "{}, {} stars, Artist: {}, Album: {}.".format(self.name, self.rating, self.artist, self.album)
    
    def __str__(self):
        return self.play()
 
    def add(self):
        name = input("Enter song name: ")
        artist = input("Enter artist: ")
        album = input("Enter album: ")
        rating = int(input("Enter rating: "))
        newSong = Song(name, rating, artist, album)
        print("Song added!")
        return newSong
    
class Picture(Media):
    def __init__(self, name, rating, dpi : int):
        self.name = name
        self.rating = rating
        self.dpi = dpi
    
    def getResolution(self):
        return self.dpi
    
    def setResolution(self, value):
        self.dpi = value
        
    def show(self):
        return "{}, {} stars, Resolution: {} dpi.".format(self.name, self.rating, self.dpi)
    
    def __str__(self):
        return self.show()
    
    def add(self):
        name = input("Enter picture name: ")
        dpi = int(input("Enter dpi: "))
        rating = int(input("Enter rating: "))
        newPicture = Picture(name, rating, dpi)
        print("Picture added!")
        return newPicture