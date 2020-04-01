def compare_strings(s1, s2):
    if len(s1) > len(s2):
        return s1
    elif len(s1) < len(s2):
        return s2
    elif s1 == s2:
        return ('Both words have the same length.')
    else:
        return ('Please enter words only, no numerics.')

def main():
    string1 = str(input('Enter first word: >> '))
    string2 = str(input('Enter second word: >> '))
    comparison = compare_strings(string1, string2)
    print(comparison)

main()
