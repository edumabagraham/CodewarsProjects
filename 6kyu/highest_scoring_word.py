import time
start = time.time()

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26}

str = 'what time are we climbing up the volcano'
str = str.split(' ')



def high(x):
    count = 0
    highest_count = 0
    for i in x:
        for j in i:
            count += dict[j]

        if (count > highest_count):
            highest_count = count
            string = i
            count = 0
        else:
            count = 0
    return string


print(high(str))

end = time.time()
print('Execution time is: ', end-start)