
def two_oldest_ages(lst):
    oldest = max(lst)
    lst.pop(lst.index(oldest))
    second_oldest = max(lst)
    return [second_oldest, oldest]

"""
# Course solution:
# I have to admit I overthought a simple one.

def two_oldest_ages(ages):
    return sorted(ages)[-2:]
"""



print(two_oldest_ages( [1, 2, 10, 8] )) # [8, 10]
print(two_oldest_ages( [6,1,9,10,4] )) # [9,10]
print(two_oldest_ages( [4,25,3,20,19,5] )) # [20,25]