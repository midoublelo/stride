# stride.
stride is a Spotify music recommendation engine that sorts recommendations into various categories.

## Usage
In order to use stride you need to create a Spotify for Developers account and add a new app. You'd probably want to just call this app stride but the name can be anything you want. When you add this app, go into the settings for it and add `http://localhost:8888/callback` as a Redirect URI. This is so you can authenticate with your Spotify account. You also need to copy down the Client ID and Client Secret and paste those into the `engine.py` file at the corresponding variables, `CLIENT_ID` and `CLIENT_SECRET`. Once this is done you can run `stride.py` and it will open up a webpage where you can accept the connection of a new app. Upon accepting you can now use stride.
## Categories
stride generates 25 recommendations each time you run it. These recommendations are based on your recent top 5 artists. You can then select different categories which take certain songs from the 25 generated recommendations. These categories are:
- Emotion [Happiest/Saddest]
- Tempo [Highest Tempo/Lowest Tempo]
- Volume [Loudest/Quietest]
- Energy [Most Energetic/Least Energetic]
- Length [Longest/Shortest]
## Requirements
stride makes use of the `spotipy` and `rich` libraries for accessing the Spotify API and for displaying the data, respectively. You can install these both automatically by using `pip install requirements.txt` in the main directory, along with `stride.py` and `engine.py`.
