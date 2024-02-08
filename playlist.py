class Playlist:

    """Playlist class represents a playlist on Spotify 

    Attributes: 

        name (str): value that shows the playlist name
        id (int): value that shows the Spotify playlist id

    """
    def __init__(self, name, id):
        
        """Initializes the instance based on playlist parameters
        
        Args:
            name: defines the name of the playlist in new instance
            id: defines the id of the playlist in the new instance
 
        """

        self.name = name
        self.id = id

    def __str__(self):

        """Returns playlist name
        
        """
        
        return f"Playlist: {self.name}"