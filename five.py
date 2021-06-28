# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    odds = list(filter(lambda x: x % 2==1, source_array)) #filter the odd numbers from the list.
    odds.sort()
    # print(odds)
    for element in range(0,len(source_array)):
        if source_array[element] % 2 == 1:
            source_array[element] = odds.pop(0)
    return source_array



print(sort_array([5,8,6,3,4]))