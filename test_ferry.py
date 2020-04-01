def using_program():
    while True:
        try:
            prompt = str(input('Do you wish to use my program (y/n)? '))
            if prompt == 'n':
                break
                print('Good bye.')
            else:
                print('Please enter y or n. >>> ')
        except ValueError:
            print('Invalid input. Please try again.')
    return prompt

def main():
    answer = using_program()
    print(f'You have chosen to continue with the program. Please enter your name >>> ')

main()


