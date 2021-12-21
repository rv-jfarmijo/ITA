def list_check(list_of_lists):
    for item in list_of_lists:
        if type(item) != list:
            return False
        pass
    return True

# better solution:

def list_check(vals):
    return all(type(l) == list for l in vals)



print(list_check([[],[1],[2,3], (1,2)])) # Fals
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True

