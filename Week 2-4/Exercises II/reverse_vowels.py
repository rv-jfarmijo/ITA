
def reverse_vowels(str):
    vowels = 'aeiou'
    current_index = 0
    indices = []
    vowel_list = []  
    str_list = [x for x in str]  
    for x in str:
        if x.lower() in vowels:
            indices.append(current_index)
            vowel_list.append(x)
        current_index +=1
    vowel_list.reverse()
    for x in zip(indices, vowel_list):
        str_list[x[0]] = x[1]
    return  ''.join(str_list)

"""
# Course solution:

def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)
"""
    


print(reverse_vowels("Hello!")) # "Holle!" 
print(reverse_vowels("Tomatoes")) # "Temotaos" 
print(reverse_vowels("Reverse Vowels In A String")) # "RivArsI Vewols en e Streng"
print(reverse_vowels("aeiou")) # "uoiea"


