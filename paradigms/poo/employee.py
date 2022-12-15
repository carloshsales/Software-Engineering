from person import Person

class Employee(Person):
    def __init__(self, age: int, name: str, occupation: str) -> None:
        super().__init__(age, name)
        self.setOccupation(occupation)

    def setOccupation(self, occupation: str):
        self.occupation = occupation;

    def getOccupation(self):
        return self.occupation

    def printTest(self):
        super().printTest()
        print(f"My occupation is {self.occupation}")