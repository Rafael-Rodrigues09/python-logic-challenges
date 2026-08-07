s = "abbac"

def find_substring(string):
    valids = {}
    begin = 0
    len_max = 0
    for index, letter in enumerate(string):        
        if letter in valids and valids[letter] >= begin:
            begin = valids[letter] + 1
            valids[letter] = index
        valids[letter] = index
        current = index - begin + 1
        if current > len_max: len_max = current
    return len_max

print(find_substring(s))

           
        
