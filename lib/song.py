class Song:
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    count = 0

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1    

    genres = []

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    artists = []

    @classmethod
    def add_to_artists(cls, artist):
        Song.artists.append(artist)     

    genre_count = 0       


    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1 