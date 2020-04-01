def compare_numbers(x, y):
    if x > y:
        return x
    elif x == y:
        return ('Both numbers must be unique.')
    else:
        return y


def main():
    num1 = int(input('Enter number 1: >> '))
    num2 = int(input('Enter number 2: >> '))
    comparison = compare_numbers(num1, num2)
    print(comparison)


main()
