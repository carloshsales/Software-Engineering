from datetime import datetime
from game import Game
from publisher import Publisher



dateGOW = datetime(2012, 6, 3)
godOfWar = Game("God Of War", dateGOW.strftime("%Y-%m-%d", ), ["action", "adventure", "puzzle"])

dateNFS = datetime(2022, 11, 10)
needForSpeed = Game("Need for Speed", dateNFS.strftime("%Y-%m-%d",), ["Arcade", "action"])

myPublisher = Publisher("MyPub", [godOfWar, needForSpeed]) #agregation

print(myPublisher.getInformation())