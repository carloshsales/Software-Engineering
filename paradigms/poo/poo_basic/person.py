class Person:
    def __init__(self, age: int, name: str) -> None:
        self.setName(name)
        self.setAge(age)

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def printTest(self):
        print(f"Hi, my name is {self.getName()} and i'm {self.getAge()} years old!")



    