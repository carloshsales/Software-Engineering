numbers_list = [9.56783, 7.57568, 3.00914, 6.2321]
precision_list = [2, 2, 3, 3]


#SOLUTION IN COLLEGE
round_items = lambda x, y: round(x, y)
result = list(map(round_items, numbers_list, precision_list))


def main():
    print(result)


if __name__ == '__main__':
    main()