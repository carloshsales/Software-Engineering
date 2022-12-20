class Game:
    def __init__(self, name: str, release: object, gender: list) -> None:
        self.setName(name)
        self.setRelease(release)
        self.setGender(gender)

    def setName(self, name: str):
        self.name = name

    def setRelease(self, release: object):
        self.release = release

    def setGender(self, gender: list):
        self.gender = gender

    def getName(self):
        return self.name
    
    def getRelease(self):
        return self.release

    def getGender(self):
        return self.gender