class Publisher:
    def __init__(self, name: str, games: list) -> None:
        self.setName(name)
        self.setGames(games)

    # @name.setter
    def setName(self, name: str) -> None:
        self.name = name
    
    # @games.setter
    def setGames(self, game: list) -> None:
        self.games = game


    def getName(self) -> str:
        return self.name


    def getGames(self) -> list:
        gameList = []
        for game in self.games:
            gameList.append({"name": game.getName(),
                "release": game.getRelease(),
                "gender": game.getGender()
            })
            
        return gameList

    def getInformation(self) -> str:
        text = f"The publisher {self.getName()} \n Games:  {self.getGames()}"
        return text