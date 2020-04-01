#  Name:  Strings and list
#  Desc:  Slicing Strings and Methods that can be used with Strings
#         Converting Strings to lists and vice versa
word1 = "Hawaii"
word2 = "Honolulu"
word2 = word1
print("Slicing works with Strings")
print(word1[0:2])
print(word1[-3:-1])
print("\nIterate over a String")
for x in word1:
    print(x)
for i,letter in enumerate(word1):
    print(i, letter)
print("\nCheck if a letter is contains in a String")
if 'H' in word1:
    print("Word1 contains H")
print("\nStrings are immutable")
#  word1[0] = 'K'   illegal
print("\nYou can use the index method to find the position of a letter:")
pos = word1.index('w')
print(f"\nw is at position {pos}  in {word1}")
number = word1.count('i')
print(f"\nThere are {number} i's in + {word1}")
