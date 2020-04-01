def convert_to_miles(km):
    ratio = 0.6214
    result = km*ratio
    return result


def main():
    distance = float(input('Enter distance in km: >>> '))
    print(f'Distance in miles: {convert_to_miles(distance):.2f} ')
    ##OR
    miles = convert_to_miles(distance)
    print(f'Distance in miles: {miles:.2f} ')

main()
