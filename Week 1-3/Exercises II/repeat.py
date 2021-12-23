
def repeat(phrase, times):
    return phrase * times

"""
# Course solutions:
#  is mine the built in repeat function?
def repeat(string, num):
    if (num == 0):
        return ''
    i = 0
    newStr = ''
    while (i < num):
        newStr += string
        i += 1
    return newStr
"""


print(repeat('*', 3)) # '***' 
print(repeat('abc', 2)) # 'abcabc' 
print(repeat('abc', 0)) # ''



