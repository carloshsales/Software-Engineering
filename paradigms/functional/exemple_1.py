# value = 10

# def multiply(factor):
#     global value

#     value = value * factor
#     print("Result: ", value)


# def main():
#     number = int(input("Isert a number: "))
#     multiply(number)
#     multiply(number)

# if __name__ == "__main__":
#     print(__name__)
#     main()

#PURE FUNCTION************************************************************************************
value = 10

def multiply(value ,factor):
    value = value * factor
    return value


def main():
    factor = int(input("Isert a number: "))
    print("Result: ", multiply(value,factor))
    print("Result: ", multiply(value, factor))

if __name__ == "__main__":
    print(__name__)
    main()