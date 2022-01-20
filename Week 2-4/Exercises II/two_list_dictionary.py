
def two_list_dictionary(dict1, dict2):
    if len(dict1) > len(dict2):
        for x in range((len(dict1)-len(dict2))):
            dict2.append(None)
    return dict(zip(dict1, dict2))

"""
# Course solution:
# were we not supposed to use zip?

def two_list_dictionary(keys, values):
    collection = {}
 
    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
        else:
            collection[keys[idx]] = None
 
    return collection

"""





print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) )# {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) )# {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['x', 'y', 'z']  , [1,2])) # {'x': 1, 'y': 2, 'z': None}