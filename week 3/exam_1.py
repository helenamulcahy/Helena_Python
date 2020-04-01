from reading_from_user import read_nonempty_alphabetical_string
from reading_from_user import read_integer

class_cost_per_student = 3.35

def heading():
    print(f"{7*'*'}")
    print('Welcome')
    print(f"{7*'*'}")


def read_data():
    name = read_nonempty_alphabetical_string('What is the instructor\'s name?  ')
    number = read_integer('How many classes did he/she teach? ')
    return name, number


def read_attendances(number):
    classes = []
    number = []
    for i in range(classes[x]):
        number_of_students = int(input(f"How many students in {classes[x]}?  "))
        number.append(number_of_students)
    return number

def display_costs(name, number_of_students):
    classes = int('How many classes? ')
    class_earnings = 3.35 * number_of_students
    average_attendance = float(sum(number_of_students) /classes)
    total = float(sum(class_earnings))
    print(f"Instructor:   {name.upper()}")
    print(f"{25*'-'}")
    i = number_of_students
    for x in range(len(class_earnings)):
       print(f"Day {classes[x]:10} €{class_earnings[x]:.2f}")
        print(f"Average attendance: {average_attendance}")
        print(f"Total due to the instructor: €{total:.2f}")

def main():
    heading()
    name, number = read_data()
    number_of_students = read_attendances(number)
    display_costs(name, number_of_students)


main()





