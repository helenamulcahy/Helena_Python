import math
def calculate_circle_area(radius):
    result = math.pi*radius**2
    return result

def main():
    number = int(input('Enter the radius of a circle: >> '))
    print(f'The area of a circle with radius {number} is: {calculate_circle_area(number):.2f}')

main()
