driver_price = 10
passenger_price = 2.50
num_of_passengers = 0
cost = 0
another = 'y'
total = 0
counter = 0


newfile = open('bookings.txt', 'w')

while another[0].lower() == "y":
    counter += 1
    name = input('Please enter your Name >>>  ')
    flag = True
    num_of_passengers = int(input('How many passengers? '))
    #while not (0 =< num_of_passengers <= 100):
        #num_of_passengers = input('Please enter number of passengers greater than zero and less than 100. >>> ')


    cost = float(driver_price + (2.50 * num_of_passengers))
    total += cost
    #print(cost)
    from datetime import date
    today = date.today()
    d1 = today.strftime("%d, %B %Y")
    #print("Date: ", d1)
    newfile.write("{}\t{}\t{}\t{}\t{}\t{}\t{}{}\t{}\n".format("Date: ", d1, "\nName:" , name.title(), "\nHow many passengers? ", num_of_passengers, "\nTotal cost: €", cost, "\n=============================="))
    print("The ticket has been printed in bookings.txt")
    print('=============================================')
    another = input("Do you wish to use my program again (y/n)? >>>>  ")

newfile.close()
