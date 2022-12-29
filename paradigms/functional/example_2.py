def mutiply(factor):
    def multi(number):
        return number * factor
    return multi

def main():
    multiply_10 = mutiply(10)
    print(multiply_10)
    print(multiply_10(1))
    print(multiply_10(2))
 
    multiply_5 = mutiply(5)
    print("==============================================================")
    print(multiply_5)
    print(multiply_5(1))
    print(multiply_5(2))

if __name__ == "__main__":
    main()