class Track:

    """Track class represents a song on Spotify 

    Attributes: 

        name (str): value that shows the track name
        id (int): value that shows the Spotify track id
        artist (str): value that shows the artist name

    """

    def __init__(self, name, id, artist):
        
        self.name = name
        self.id = id 
        self.artist = artist 

    def create_spotify_uri (self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return f"{self.name} by {self.artist}" 