import json
import requests
from track import Track
from playlist import Playlist


class SpotifyClient:

     """SpotifyClient performs operations using Spotify API
     
     Attributes:

          authorization_token (str): Spotify API token
          user_id (int): Spotify user id
     
     """

     def __init__(self, authorization_token, user_id):

          """Initiliazes the instance based on user's individual token and id
          
          Args:
               authorization_token: defines the api token in new instance
               user_id: defines the individual user's id in new instance
          
          """

          self.authorization_token = authorization_token
          self.user_id = user_id

     def get_last_played_tracks (self, limit=10):

          """Get n number of last played tracks of a Spotify user
          
          Args:
               limit(int): Number of tracks to retrieve.

          """

          url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
          response = self._place_get_api_request(url)
          response_json = response.json()
          print (response_json)
          print (f" ")
          tracks = [Track(track["track"]["name"], track ["track"] ["id"], track["track"]["artists"][0]["name"]) for track in response_json["items"]]
          return tracks 
     
     def get_track_recommendations(self, seed_tracks, limit=50):

          """Get a list of recommended tracks based on a number of given seed tracks

          Args:
               seed_tracks (list): A list of tracks to be used for creating recommendations
               limit (int): Number of recommended tracks to retrieve 

          """
          
          seed_tracks_url = ""
          for seed_track in seed_tracks:
               seed_tracks_url += seed_track.id + ","
          seed_tracks_url = seed_tracks_url [:-1]
          url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
          response = self._place_get_api_request(url)
          response_json = response.json()
          tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for track in response_json["tracks"]]
          return tracks 
     
     def _place_get_api_request (self, url):

          """Requests content from the Spotify api itself using authorization token and url
          
          Args:
               url(string): Specific url to be used by the Spotify api to know what is being requested
          
          """

          response = requests.get(
               url,
               headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.authorization_token}",
                    "Accept": "application/json"
               }
          )
          return response
     
     def create_playlist (self, name):

          """Creates playlist using the Spotify api
          
          Args:
               name(string): name of the playlist
          
          """

          data = json.dumps({

               "name": name, 
               "description": "Recommended tracks"
          })

          url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
          response = self._place_post_api_request(url, data)
          response_json = response.json()
          
          playlist_id = response_json["id"]
          playlist = Playlist (name, playlist_id)
          return playlist
     
     def _place_post_api_request (self, url, data):

          """Makes a call to the Spotify API for data using authorization token
          
          Args:
               url(string): Specific url to be used by the Spotify api to know what is being requested
               data: Json data on the tracks to be added and used for the playlist
          
          """

          response = requests.post(
               url,
               data = data,
               headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.authorization_token}"                    
               }
          )
     
     def populate_playlist(self, playlist, tracks):

          """Requests content from the Spotify api itself using authorization token and url
          
          Args:
               playlist: Playlist that was created for recommended tracks
               tracks: Recommended tracks to be added to the playlist
          
          """
                    
          track_uris = [track.create_spotify_uri() for track in tracks]
          data = json.dumps(track_uris)
          url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
          response =self._place_post_api_request(url,data)
          response_json = response.json()
          return response_json

