from datetime import date
today = date.today()
d1 = today.strftime("%d, %B %Y")
#print("Date: ", d1)

def read_nonempty_alphabetical_string(prompt):
    while True:
        s = input(prompt)
        s_with_no_spaces = s.replace(' ', '')
        if len(s_with_no_spaces) > 0 and s_with_no_spaces.isalpha():
            break
        else:
            print("Please type letters only")
    return s


def read_fullname():
    f = read_nonempty_alphabetical_string("Firstname >>> ")
    s = read_nonempty_alphabetical_string("Surname >>> ")
    return f, s

def read_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                break
            else:
                print('Non-negative numbers, please...')
        except ValueError:
            print('Must be numeric...')
    return number


def number_of_passengers():
    x = read_positive_integer('How many passengers? ')
    return x

def ticket_cost(x):
    return x

def display_ticket_details(f,s, passengers, cost, output_file=None):
    print(f"Name>>>  {f} {s}", file= output_file)
    print(f"Number of passengers:   {p}", file= output_file)
    print(f"Total cost: € 10 + ticket_cost", file= output_file)


def main():
    firstname, surname = read_fullname()
    #print(f'Name >>> {firstname.title()} {surname.title()}')
    passengers = number_of_passengers()
    #print(f'Number of passengers: {passengers}')
    ticket_details = display_ticket_details({f}, {s}, p, cost)
    print('The ticket has been printed in output.txt file.')
    display_ticket_cost = ticket_cost(10 + (2.5 * number_of_passengers()))

main()



