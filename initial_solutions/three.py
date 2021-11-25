# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
#
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    s = list(s.casefold())

    o = list(filter(lambda i: i == 'o', s))
    x = list(filter(lambda  i : i == 'x', s))

    if (len(o) == len(x)):
        return True

    return False

# Other solutions
# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')

# def xo(s):
#     s = list(s.casefold())
#
#     if s.count('x') == s.count('o'):
#         return True
#     return False

