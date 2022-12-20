from poo_basic.person import Person

class Employee(Person):
    def __init__(self, age: int, name: str, occupation: str, salary: object) -> None:
        super().__init__(age, name)
        self.setOccupation(occupation)
        self.setSalary(salary)

    def setOccupation(self, occupation: str) -> None:
        self.occupation = occupation;

    def setSalary(self, salary: object) -> None:
        self.salary = salary

    def getOccupation(self) -> str:
        return self.occupation

    def getSalary(self) -> float:
        return self.salary.getAmount()

    def printTest(self) -> None:
        super().printTest()
        print(f"My occupation is {self.occupation}")
        print(f"My salary is ${self.getSalary()},00")