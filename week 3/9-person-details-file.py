# This example illustrates how we can use the default value of the
# parameter to write to strings.

from reading_from_user import read_nonempty_alphabetical_string
from reading_from_user import read_positive_integer
from reading_from_user import read_percentage_float


def read_fullname():
    f = read_nonempty_alphabetical_string("Firstname >>> ")
    s = read_nonempty_alphabetical_string("Surname >>> ")
    return f, s


def read_personal_details():
    firstname, surname = read_fullname()
    prompt = firstname+"'s Age >>> "
    age = read_positive_integer(prompt)
    prompt = firstname + "'s grade >>> "
    grade = read_percentage_float(prompt)
    return firstname, surname, age, grade

# We assume that the user wishes to print to the screen, so
# the parameter output_file is set to None by default.
# If we wish to write to a file, we can specify the file connection
# as an argument in the function call.
def display_personal_details(f,s,a,g, output_file=None):
    print(f"Name:  {f} {s}", file= output_file)
    print(f"Age:   {a}", file= output_file)
    print(f"Grade: {g:.0f}%", file= output_file)


def main():
    student_firstname, student_surname, student_age, student_grade = read_personal_details()

    with open("output.txt", "w") as output:
        display_personal_details(student_firstname, student_surname, student_age, student_grade, output)

    display_personal_details(student_firstname, student_surname, student_age, student_grade)


main()