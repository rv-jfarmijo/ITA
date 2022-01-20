

def mode(lst):
    counts = {}
    for x in lst:
        if x in counts.keys():
            counts[x] +=1
        else:
            counts[x] = 1
    mode_key = max(counts, key=counts.get)
    return mode_key


"""
# Course solution:

def mode(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]
"""


print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4