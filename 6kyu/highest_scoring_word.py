dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26}

str = 'take me to semynak'
str = str.split(' ')
print(str)
count = 0
highest_count = 0



for i in str:

    for j in i:
        count += dict[j]

    if (count > highest_count):
        highest_count = count
        string = i
        count = 0
    else:
        count = 0



print(highest_count)
print(string)
