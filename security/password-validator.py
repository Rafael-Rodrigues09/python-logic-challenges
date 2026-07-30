passwords = ["senha123", "Admin@2026", "bunker", "Rafael99", "admin_root1", "Grt5"]
def valid_pass(passes):
    valids = []
    for word in passes:
        if len(word) < 8: continue
        if 'admin' in word.lower(): continue
        is_number = False
        is_upper = False
        for letter in word:
            if letter.isdigit(): is_number = True
            if letter.isupper(): is_upper = True
        if is_number and is_upper: valids.append(word)    
    return valids

print(valid_pass(passwords))

        