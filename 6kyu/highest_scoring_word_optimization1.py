import time
start = time.time()

str = 'd bb'
str = str.split(' ')



def high(x):
    highest_count = 0
    for i in x:
        count = sum([ord(j) - 96 for j in i])
        if count > highest_count:
            highest_count = count
            string = i

    return string


print(high(str))
end = time.time()
print('Execution time is: ', end-start)