def first_non_repeating_letter(string):
    if first(string) ==None:
        return ''
    else:
        return first(string)

def first(str):
    count = 0
    if len(str) == 0:
        return ''
    else:
        for i in str:
            for j in str:
                if i.lower() == j.lower():
                    count += 1
            if count > 1:
                count = 0
            else:
                return i
            # break


string = 'aa'
print(first_non_repeating_letter(string))
# print(first_non_repeating_letter(str))
# string = ''
# count = 0
# for i in str:
#     # count += 1
#     string += i
#     for j in str[1:]:
#         if string == j:
#             count += 1

# print(count)
