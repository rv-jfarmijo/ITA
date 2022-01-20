
def vowel_count(strinput):
    raw_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for x in strinput:
        if x.lower() in raw_count.keys():
            raw_count[x.lower()] +=1
    return {k:v for (k,v) in raw_count.items() if v != 0}


"""
# Course solution:
def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}

"""


vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}