def isPrime(number: int) -> bool:
    count = 0
    if not(number < 2):
        for key in range(1, number + 1):
        if number % key == 0:
            count += 1
        
    if count == 2:
        return True
    
    return False