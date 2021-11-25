# def iq_test():
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
# iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

# iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd


# Mine solution
def iq_test(numbers):
    numbers = list(map(int, numbers.split()))

    even = list(filter(lambda i: (i % 2 == 0), numbers))
    odd = list(filter(lambda i: (i % 2 == 1), numbers))

    if (len(even) == 1):
        return numbers.index(even[0]) + 1
    else:
        return numbers.index(odd[0]) + 1

iq_test('1 1 2 1')


# Other solution
# ONE
# def iq_test(numbers):
#     e = [int(i) % 2 == 0 for i in numbers.split()]
#
#     return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


# TWO
# def iq_test(n):
#     n = [int(i)%2 for i in n.split()]
#     if n.count(0)>1:
#         return n.index(1)+1
#     else:
#         return n.index(0)+1
