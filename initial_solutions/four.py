# #              1
# #           3     5
# #        7     9    11
# #    13    15    17    19
# # 21    23    25    27    29
# # ...
#
#
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.:
#
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

def rowSumOddNumbers(n):
  return pow(n, 3)

print(rowSumOddNumbers(5))
# Other solutions
# def rowSumOddNumbers(n):
#   return n*n*n

# def row_sum_odd_numbers(n):
#     if type(n)==int and n>0:
#         return n**3
#     else:
#         return "Input a positive integer"

