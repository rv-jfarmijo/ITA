def find_the_duplicate(arr):
    counts = {x:arr.count(x) for x in arr if arr.count(x) > 1}
    if counts.keys():
        return list(counts.keys())[0]

"""
# Course solution"

def find_the_duplicate(arr):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)
"""




print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None