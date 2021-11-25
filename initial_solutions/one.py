#my solution which does'nt work lol
# def array_diff(arrayA, arrayB):
#     for i in arrayA:
#         for element in arrayB:
#             if i == element:
#                 arrayC.remove(i)
#     return arrayC
#
# # THis compares it from index 0 through to the end but does not come back therefore it does
# arrayA = [5, -14, 1, 16, -18, 2, -18, -14, -1, -1, 7, 0, 3, -6, 2, 1]
# arrayB = [16, -19, 8, 11, -17, -20, 13, 17, -14, -15, -14, -11]
# arrayC = arrayA[:]
#
# print('array_diff= ', array_diff(arrayA,arrayB))

#
# def array_diff(arrayA, arrayB):
#     for b in arrayB:
#         if b in arrayA:
#             #delete all occurences of b in arrayA
#             arrayA = remove_all_b(arrayA, b)
#     return arrayA
#
# def remove_all_b(arrayA, b):
#     return list(filter(lambda a: a != b, arrayA))
#
#
# print(array_diff([1,2,3],[1,2]))



def array_diff(a, b):
    return [x for x in a if x not in b]

print(array_diff([1,2,3],[1,2]))