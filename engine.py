import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ENTER CLIENT ID"
CLIENT_SECRET = "ENTER CLIENT SECRET"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-top-read"))

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