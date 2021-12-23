
def sum_up_diagonals(lst):
    total = 0
    length = len(lst[0])
    x = 0
    y = length - 1
    while x < length and y > -1:
        total += lst[x][x] + lst[x][y]
        x+=1
        y-=1
    return total

"""
# Course solution:
# I forgot all about enumerate. look more into  that

def sum_up_diagonals(arr):
    total = 0
    
    for i,val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total
"""


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals(list1)) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
print(sum_up_diagonals(list2)) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

print(sum_up_diagonals(list3)) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
print(sum_up_diagonals(list4))# 68