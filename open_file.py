def openfile(file_name):
    connection = open(file_name)
    contents = connection.read().upper()
    print(contents)

def main():
    openfile("TEST.txt")
    openfile("ten_bottles.py")

main()
