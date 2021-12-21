

def running_average():
    running_average.total = 0
    running_average.amount = 0
  
    def average(num):
        running_average.total += num
        running_average.amount += 1
        return running_average.total / running_average.amount
    
    return average



"""
# Course solution:

def running_average():
    running_average.accumulator = 0
    running_average.size = 0
  
    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size
    
    return inner
"""



rAvg = running_average()
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11

rAvg2 = running_average()
print(rAvg2(1)) # 1
print(rAvg2(3)) # 2