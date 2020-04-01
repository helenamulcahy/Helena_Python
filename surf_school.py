school_name = 'The Salty Sea Surf'
beginner_price = 10.25
advanced_price = 14.75
cost = 0
another = "yes"
total = 0
counter = 0

try:
    newfile = open("bookings.txt", 'w')
    newfile.write("~~~~~~~~" + school_name + "~~~~~~~~\n")
    newfile.write("No." + "\tName" + "\tSurname  " + "\tLevel" + "\tCost\n")
    newfile.write("--------------------------------\n")

    while another[0].lower() == "y":
        counter += 1
        first_name = input('Please enter your First Name:  ')
        flag = True

        while flag:
            if len(first_name) < 2:
                first_name = input("Name has to be at least 2 characters long >>> ")
            else:
                for i in range(len(first_name)): #going through all letters in the input
                    if first_name[i].isalpha() and i == len(first_name) -1:#if letter in name is a letter and is last, that means all word was letters only we set flag to false so it would exit while loop
                        flag = False
                    elif first_name[i].isalpha():#this one deals with all chars that are letters but not last
                        continue
                    else:#if digit or any other char thats not letter encountered asks for new input and breaks for loop
                        first_name = input("Name can only contain letters and must be at least 2 characters long >>> ")
                        break
        #same for last name
        last_name = input('Please enter your Last Name: ')
        flag = True

        while flag:
            if len(last_name) < 2:
                last_name = input('Last Name has to be at least 2 letters long, please re-enter >>  ')
            else:
                for i in range(len(last_name)):  # going through all letters in the input
                    if last_name[i].isalpha() and i == len(last_name) - 1:  # if letter in name is a letter and is last, that means all word was letters only we set flag to false so it would exit while loop
                        flag = False
                    elif last_name[i].isalpha():  # this one deals with all chars that are letters but not last
                        continue
                    else:  # if digit or any other char thats not letter encountered asks for new input and breaks for loop
                        last_name = input("Name can only contain letters and must be at least 2 characters long >>> ")
                        break

        level = input('Please enter your level by selecting 1 or 2.'  # the validation for this we done on your project
                  '\n\t1: Beginner' \
                  '\n\t2: Advanced' \
                  '\n ==> ')
        while not (level in "12" and len(level) == 1):
            level = input('Please select "1" for Beginner or "2" for Advanced.>>>')
        level = int(level) # once we sure its valid number we convert it to int
        coupon_code = str(input('Please enter the discount code:  '))
        if len(coupon_code) == 4 and coupon_code[:2] == 'SS':
            print('Valid code: 2 euros discount will apply. ')
            discount = 2  # just to track was discount code was correct
        else:
            print("Discount code is invalid.")
            discount = 0  # same here
        if level == 1:
            cost = beginner_price - discount  # depending on discount code whether it's 0 or 2
            total += cost
            print(cost)
            newfile.write("{}\t{}\t{}\t{}\t{}\n".format(counter, first_name, last_name, "     Beginner", cost))
        else:
            cost = advanced_price - discount
            total += cost
            print(cost)
            newfile.write("{}\t{}\t{}\t{}\t{}\n".format(counter, first_name, last_name, "     Advanced", cost))
        another = input("Would you like to add another person? (y/n)>>>>  ")


except:
    print('Invalid input. Please check your input and try again.')
finally:
    newfile.write("No. of people booked:\t{}\n".format(counter))
    newfile.write("Total Cost:\t{}\n".format(total))
    newfile.close()
