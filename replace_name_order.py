def replace_order(x,y):
    return y + ", " + x

def main():
    first_name = str(input('Enter First Name: >> '))
    last_name = str(input('Enter Last Name: >> '))
    order = replace_order(first_name, last_name)
    print(order)


main()
