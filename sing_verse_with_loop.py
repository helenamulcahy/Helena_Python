def sing_verse(x):
    print(x, "green bottles hanging on the wall,")
    print(x, "green bottles hanging on the wall,")
    print("And if one green bottle should accidentally fall,")
    print("There'll be", x-1, "green bottles hanging on the wall.")

def main():
    for i in range(10,1,-1):
        sing_verse(i)

main()
