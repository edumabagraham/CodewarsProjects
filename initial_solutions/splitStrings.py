def splitString(s):
    # if length of arr is odd append underscore
    if len(s) % 2 == 1:
        s = s + '_'
    n = 2
    split_String = [s[i:i + n] for i in range(0, len(s), n)]
    return split_String


    # return a list sliced by 2 for the arr

#----Optimized one

def splitString(s):
    return [s[i:i +2] if i < len(s) - 1 else s[-1] + '_' for i in range(0,len(s),2)]