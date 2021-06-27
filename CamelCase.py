def camel_case(string):
    string = string.split()
    s = "".join(word[0].upper() + word[1:].lower() for word in string)
    return s


print(camel_case('Basic tests'))

# txt = "welcome to the jungle"
#
# x = txt.split()
#
# print(x)


# def solve(words):
#       s = "".join(word[0].upper() + word[1:].lower() for word in words)
#       return s[0].lower() + s[1:]
#       # ob = Solution()
# words = ["Hello", "World", "Python", "Programming"]
# print(solve(words))


