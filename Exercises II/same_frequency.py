

def same_frequency(num1, num2):
    digits = [char for char in '0123456789']
    d1 = {x:str(num1).count(x) for x in digits}
    d2 = {x:str(num2).count(x) for x in digits}
    return d1 == d2
    
"""
# Course solution:
# Did I miss something with my logic?
# No, I just preempted the need for a key comparison.

def same_frequency(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
  
    for key,val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True
"""


print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True