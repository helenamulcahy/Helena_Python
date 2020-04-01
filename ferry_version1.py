def display_ticket_details(f,s, passengers, cost, output_file=None):
    print(f"Name>>>  {f} {s}", file= output_file)
    print(f"Number of passengers:   {p}", file= output_file)
    print(f"Total cost: € 10 + {2.5 * p:.2f}", file= output_file)


def main():
    firstname, surname, passengers, cost = display_ticket_details()

    with open("output.txt", "w") as output:
        display_ticket_details()

main()
