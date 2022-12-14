def factorialResult(number: int) -> int:
    result = 0

    if number == 0 or number == 1:
        return 1

    for indicie in range(1, number + 1):
        result += factorialResult(number - 1)

    return result
    