



def letter_counter(str):
    letters_dict = {}
    for x in str:
        if x.lower() in letters_dict.keys():
            letters_dict[x.lower()] += 1
        else:
            letters_dict[x.lower()] = 1
    def letters(ltr):
        return letters_dict[ltr]
    return letters




counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1 