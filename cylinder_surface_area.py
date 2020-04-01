import math
def calculate_cylinder_area(x, y):
    result = ((2*math.pi*x*y) + (2*math.pi*x**2))
    return result

def main():
    radius = int(input('Enter the radius of a cylinder: >> '))
    height = int(input('Enter the height of a cylinder: >> '))
    cylinder_area = calculate_cylinder_area(radius, height)
    print(f'The surface area of the cylinder is: {cylinder_area:.2f}')


main()
