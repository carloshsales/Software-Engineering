class Salary:
    def __init__(self, base: float, add: float = None) -> None:
        self.setBase(base)
        self.setAdd(add)

    def setBase(self, base: float) -> None:
        self.base = base

    def setAdd(self, add: float) -> None:
        self.add = add

    def getAmount(self) -> float:
        return (self.base + self.add) * 12

