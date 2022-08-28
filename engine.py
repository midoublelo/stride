import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ENTER CLIENT ID"
CLIENT_SECRET = "ENTER CLIENT SECRET"

PLAYLIST_FORMAT = {
    "name": "stride.",
    "description": "auto-generated playlist from stride."
}

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-top-read playlist-modify-public playlist-modify-private"))

def generateRecommendations():
    global recommendedTID
    global songs
    artistResult = sp.current_user_top_artists(time_range="short_term", limit=19)
    for i in range(19):
        topArtists = []
        for i, item in enumerate(artistResult['items']):
            topArtists.append(item['id'])
    overallRecommendations = sp.recommendations(seed_artists=topArtists[0:5], limit=25)
    recommendedTID = []
    songs = {}
    for track in overallRecommendations['tracks']:
        recommendedTID.append(track['uri'])
        songs[f"{track['artists'][0]['name']}"] = f"{track['name']}"

generateRecommendations()

recommendedFeatures = sp.audio_features(tracks=recommendedTID)

happySong = max(recommendedFeatures, key=lambda ev: ev['valence'])
sadSong = min(recommendedFeatures, key=lambda ev: ev['valence'])

fastestSong = max(recommendedFeatures, key=lambda ev: ev['tempo'])
slowestSong = min(recommendedFeatures, key=lambda ev: ev['tempo'])

loudestSong = max(recommendedFeatures, key=lambda ev: ev['loudness'])
quietestSong = min(recommendedFeatures, key=lambda ev: ev['loudness'])

longestSong = max(recommendedFeatures, key=lambda ev: ev['duration_ms'])
shortestSong = min(recommendedFeatures, key=lambda ev: ev['duration_ms'])

mostEnergeticSong = max(recommendedFeatures, key=lambda ev: ev['energy'])
leastEnergeticSong = min(recommendedFeatures, key=lambda ev: ev['energy'])

def createPlaylist():
        user_id = sp.me()['id']
        playlists = sp.user_playlists(user_id)
        for i in range(len(playlists['items'])):
            if playlists['items'][i]['name'] == PLAYLIST_FORMAT['name']:
                if playlists['items'][i]['description'] == PLAYLIST_FORMAT['description']:
                    sp.user_playlist_replace_tracks(user_id, playlists['items'][i]['id'], recommendedTID)
                    print("updated spotify playlist.")
                    break
        else:
            playlist = sp.user_playlist_create(user_id, PLAYLIST_FORMAT['name'], public=True, description=PLAYLIST_FORMAT['description'])
            sp.user_playlist_add_tracks(user_id, playlist["id"], recommendedTID)
            print("created new spotify playlist.")
