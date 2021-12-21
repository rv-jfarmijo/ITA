

def find_greater_numbers(lst):
    if len(lst) == 0:
        return 0
    else:
        lcount = 0
        for x in lst:
            for y in lst[lst.index(x)+1:]:
                if x<y:
                    lcount +=1
        return lcount

"""
# Course solution:

def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j+=1
        j = i+1
        i+=1
    return count;
"""


print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0


