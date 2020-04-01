def heading():
    print('-' * 13)

    print('BPM Processor')

    print('-' * 13)



def read_positive_integer(prompt):
    while True:

        try:

            number = int(input(prompt))

            if number > 0:

                break

            else:

                print('Non-negative numbers, please...')

        except ValueError:

            print('Must be numeric...')

    return number


def read_patient_details():
    patient_number = read_positive_integer('Patient number >>> ')

    age = read_positive_integer('Age >>> ')

    return patient_number, age

def read_bpms():
    days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    bpm = []
    for i in range(7):
        b = int(input(f'BPM for {days_of_the_week[i]}: '))
        bpm.append(b)
    return bpm


def main():
    heading()
    patient_number, age = read_patient_details()
    bmp = read_bpms()
    print(bmp)
    print(f'Patient number: {patient_number} ({age} years)')
    print('=' * 35)



main()

