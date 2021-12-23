


def includes(collection, value, sindex=0):
    if type(collection) == dict:
        test_group = list(collection.values())
    else:
        test_group = collection[sindex:]
    return value in test_group

    

"""
# Course solution:
def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]
"""



print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False



