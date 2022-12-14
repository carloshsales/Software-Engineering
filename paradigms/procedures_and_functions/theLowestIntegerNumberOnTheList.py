def theLowestIntegerNumberOnTheList(numberList: list) -> int:
    result = numberList[0]
    for number in numberList:
        if(number < result):
            result = number
    return result
