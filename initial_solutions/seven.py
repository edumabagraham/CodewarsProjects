# def anagrams(word, words):
#     arr = []
#     word = sorted(word)
#     # print(word)
#     for i in range(0, len(words)):
#         words[i] = sorted(words[i])
#         #             check if the sorted strings are the same
#         #         print(words[i])
#         if word == words[i]:
#             words[i]= list("".join(map(str,words[i])))
#             print(words[i])
#              # return words[i]
#
#
# def listToString(arr)


def anagrams(word,words):
    anagram = []
    word = "".join(sorted(word))
    copy = words[:]
    for i in range(0,len(words)):
        words[i] = "".join(sorted(words[i]))
        if word.lower() == words[i].lower():
            anagram.append(copy[i])
    return anagram


# def anagrams(word,words):
#     return [item for item in words if word.sorted() == words[item].sorted()]
#
#
#


# words =['aabb', 'abcd', 'bbaa', 'dada']
# word = 'abba'
#
#
# print(list(filter(anagram, words)))
#
#
print(anagrams('abba',['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
