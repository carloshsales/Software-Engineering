from isEven import isEven

def sumAllEvenNumbersOnTheList(numberList: list) -> int:
    result = 0
    for number in numberList:
        if isEven(number):
            result += number

    return result