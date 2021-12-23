



def sum_pairs(iList, target):
    newList = iList
    while len(newList) > 1:
        a = newList.pop(0)
        for x in newList:
            if a + x == target:
                return [a, x]
    return []

"""
#  Course solution:

def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []

"""    


sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []        