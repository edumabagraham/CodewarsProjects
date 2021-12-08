# Complete the solution so that the function
# will break up camel casing, using a space between words.
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# Solution 1
def solution(s):
    bldrs = [[s[0]]]  # Store first character
    for c in s[1:]:
        if bldrs[-1][-1].islower() and c.isupper():
            bldrs.append([c])
        else:
            bldrs[-1].append(c)
    joinedString = [''.join(bldr) for bldr in bldrs]

    # Convert to string using join
    return ' '.join(joinedString)

# # Convert to string using list comprehension
# print(' '.join([i for i in joinedString]))
#
# # Convert to string using map
# print(' '.join(map(str, joinedString)))
print(solution('camelCase'))


# Solution 2
def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr

# Solution 3
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

print(solution('camelCase'))











# import re
# name = 'camelCaseT'
# splitted = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', name)).split()
# print(splitted)




