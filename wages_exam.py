def read_nonempty_alphabetical_string(prompt):
    something_is_wrong = True
    while something_is_wrong:
        s = input(prompt)
        copy_without_spaces = s.replace(" ", "")
        if len(s) > 0 and copy_without_spaces.isalpha():
            something_is_wrong = False
        else:
            print("Letters only please...")
    return s


def read_positive_integer(prompt):
    something_is_wrong= True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            something_is_wrong = number <= 0
            if number <= 0:
                print("Number must be positive")
        except:
            print("Must be numeric...")
    return number

def get_data():
    name = read_nonempty_alphabetical_string('Name >>> ')
    age = read_positive_integer('Age >>> ')
    return name, age

def get_wages():
    days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    wages = []
    for i in range(5):
        x = float(input(f'Wages for {days_of_the_week[i]} €'))
        wages.append(x)
    return wages

def display_stats(name, age, wages):
    wages = get_wages()
    name, age = get_data()
    for item in wages:
        print(item)
    return name, age, wages

def main():
    days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    name, age = get_data()
    print(f'Name:   {name.upper()}')
    print(f'Age:   {age}')
    wages = get_wages()
    print(wages)
    y = max(wages[i])
    display_stats(name, age, wages)
    print(display_stats)
    print(f'The most money was € {y} earned on {days_of_the_week[i]}.')
    #print(f'{days_of_the_week[i]} € wages[i] ')
    #print_goodbye()

main()
