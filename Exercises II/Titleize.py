

def titleize(sentence):
    words = [list(word) for word in sentence.split()]
    for x in words:
        x[0] = x[0].upper()
    return ' '.join([''.join(x) for x in words])

"""
# Course solution:
#  more elegant but harder to read.
def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))
"""



print(titleize('this is awesome')) # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
