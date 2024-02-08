import os
from spotify_client import SpotifyClient

def main():

    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"), os.getenv("SPOTIFY_USER_ID"))

    num_tracks_to_visualize = int(input("How many tracks would you like to visualize?"))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualize)

    print(f"Here are the last {num_tracks_to_visualize} tracks you listened to on Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index+1}- {track}")

    indexes = input(f"Enter a list of up to 5 tracks you'd like to use as seeds. Use indexes seperated by a space:")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks[int(index)-1] for index in indexes]

    recommeneded_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print(f"Here are the recommended tracks that will be included in a new playlist:")
    for index, track in enumerate(recommeneded_tracks):
        print(f"{index+1}- {track}")


    playlist_name = input(f"Enter the playlist name:")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"Playlist '{playlist.name} was created")

    spotify_client.populate_playlist(playlist, recommeneded_tracks)
    print (f"Recommended tracks were uploaded to playlist")

if __name__ == "__main__":

    main()


    