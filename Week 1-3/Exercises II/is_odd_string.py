
def is_odd_string(comment):
    alpha = [x for x in 'abcdefghijklmnopqrstuvwxyz']
    total = 0
    for x in comment:
        total += alpha.index(x) +1
    if total % 2 ==0:
        return False
    return True

"""
# Course solution:
# what is ord()?

def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1
"""



print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False


