PAY_PER_STUDENT_PER_CLASS = 3.35

def read_nonempty_alphabetical_string(prompt):
    while True:
        s = input(prompt)
        copy_without_spaces = s.replace(" ", "")
        if len(s) > 0 and copy_without_spaces.isalpha():
            return s
        else:
            print("Letters only please...")


def read_nonnegative_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                return number
            else:
                print("Non-negative numbers please...")
        except ValueError:
            print("Must be numeric...")


def heading():
    print(7 * "*")
    print("Welcome")
    print(7 * "*")


# Validation was not required.
def read_data():
    instructor_name = read_nonempty_alphabetical_string("What is the instructor's name? ")
    number_of_classes = read_nonnegative_integer(f"How many classes did {instructor_name} teach? ")
    return instructor_name, number_of_classes


def read_attendances(number_of_classes):
    print()
    attendances = []
    for i in range(number_of_classes):
        attendances.append(read_nonnegative_integer(f"How many students in class # {i+1}? "))
    return attendances


def display_costs(name, attendances):
    print()
    print("Instructor:", name)
    print((12+len(name))*'-')
    for i, n in enumerate(attendances):
        cost = n * PAY_PER_STUDENT_PER_CLASS
        print(f"Day {i+1}: €{cost:.2f}")
    total = sum(attendances)
    print()
    print(f"Average attendance: {total/len(attendances)}")
    print()
    print(f"TOTAL DUE TO {name.upper()}: €{total*PAY_PER_STUDENT_PER_CLASS:.2f}")


def main():
    heading()
    name, number = read_data()
    number_of_students = read_attendances(number)
    display_costs(name, number_of_students)

main()
