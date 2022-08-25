import engine

from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

APPNAME = "stride."
while True:
    option = Prompt.ask("select option/category (exit to close)", choices=["all", "playlist", "emotion", "tempo", "volume", "energy", "length", "exit"], default="all")
    if option == "all":
        allRecommendations = Table(title="all recommendations.")
        allRecommendations.add_column("artist.")
        allRecommendations.add_column("title.")
        artists = list(engine.songs.keys())
        titles = list(engine.songs.values())
        for i in range(len(engine.songs)):
            allRecommendations.add_row(artists[i], titles[i])
        mainScreen = Panel(allRecommendations, title=f"{APPNAME}")
    if option == "playlist":
        allRecommendations = Table(title="all recommendations.")
        allRecommendations.add_column("artist.")
        allRecommendations.add_column("title.")
        artists = list(engine.songs.keys())
        titles = list(engine.songs.values())
        for i in range(len(engine.songs)):
            allRecommendations.add_row(artists[i], titles[i])
        mainScreen = Panel(allRecommendations, title=f"{APPNAME}")
        engine.createPlaylist()
    elif option == "emotion":
        emotionRecommendations = Table(title="emotion recommendations.")
        emotionRecommendations.add_column("artist.")
        emotionRecommendations.add_column("title.")
        emotionRecommendations.add_column("emotion.")
        emotionRecommendations.add_row(
            engine.sp.track(engine.happySong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.happySong['id'])['name'],
            "happiest song.")
        emotionRecommendations.add_row(
            engine.sp.track(engine.sadSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.sadSong['id'])['name'],
            "saddest song.")
        mainScreen = Panel(emotionRecommendations, title=f"{APPNAME}")
    elif option == "tempo":
        tempoRecommendations = Table(title="tempo recommendations.")
        tempoRecommendations.add_column("artist.")
        tempoRecommendations.add_column("title.")
        tempoRecommendations.add_column("type.")
        tempoRecommendations.add_row(
            engine.sp.track(engine.fastestSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.fastestSong['id'])['name'],
            "highest tempo song.")
        tempoRecommendations.add_row(
            engine.sp.track(engine.slowestSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.slowestSong['id'])['name'],
            "lowest tempo song.")
        mainScreen = Panel(tempoRecommendations, title=f"{APPNAME}")
    elif option == "volume":
        volumeRecommendations = Table(title="volume recommendations.")
        volumeRecommendations.add_column("artist.")
        volumeRecommendations.add_column("title.")
        volumeRecommendations.add_column("type.")
        volumeRecommendations.add_row(
            engine.sp.track(engine.loudestSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.loudestSong['id'])['name'],
            "loudest song.")
        volumeRecommendations.add_row(
            engine.sp.track(engine.quietestSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.quietestSong['id'])['name'],
            "quietest song.")
        mainScreen = Panel(volumeRecommendations, title=f"{APPNAME}")
    elif option == "energy":
        energyRecommendations = Table(title="energy recommendations.")
        energyRecommendations.add_column("artist.")
        energyRecommendations.add_column("title.")
        energyRecommendations.add_column("type.")
        energyRecommendations.add_row(
            engine.sp.track(engine.mostEnergeticSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.mostEnergeticSong['id'])['name'],
            "most energetic song.")
        energyRecommendations.add_row(
            engine.sp.track(engine.leastEnergeticSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.leastEnergeticSong['id'])['name'],
            "least energetic song song.")
        mainScreen = Panel(energyRecommendations, title=f"{APPNAME}")
    elif option == "length":
        lengthRecommendations = Table(title="length recommendations.")
        lengthRecommendations.add_column("artist.")
        lengthRecommendations.add_column("title.")
        lengthRecommendations.add_column("type.")
        lengthRecommendations.add_row(
            engine.sp.track(engine.longestSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.longestSong['id'])['name'],
            "longest song.")
        lengthRecommendations.add_row(
            engine.sp.track(engine.shortestSong['id'])['artists'][0]['name'], 
            engine.sp.track(engine.shortestSong['id'])['name'],
            "shortest song.")
        mainScreen = Panel(lengthRecommendations, title=f"{APPNAME}")
    if option == "exit":
        print("bye...")
        break
    print(mainScreen)