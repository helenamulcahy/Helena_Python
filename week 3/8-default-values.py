# This example illustrates the use of default parameters values.
# Because most people have eyebrows, we will assume the parameters is True.
# Therefore the programmer only needs to tell us about exceptional cases.

def draw_eyes(has_brows = True):
    '''If parameters is True, draw eyebrows & eyes otherwise just the eyes.'''
    if has_brows:
        print("----")
    print("@  @")

def main():
    draw_eyes()
    print()
    draw_eyes(False)

main()