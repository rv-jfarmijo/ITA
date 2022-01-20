
def three_odd_numbers(lst):
    for x in range(0,len(lst)-1):
        try:
            if (lst[x] + lst[x+1] + lst[x+2]) % 2 != 0:
                return True
        except IndexError:
            return False
    return False



print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False