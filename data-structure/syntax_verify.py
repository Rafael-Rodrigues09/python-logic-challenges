sytax = "())"

def syntax_verify(syntax):
    dict_valids = {'}': '{', ']': '[', ')': '('}
    stack = []
    for letter in syntax:
        if letter in dict_valids:
            if not stack: return False
            if dict_valids[letter] != stack.pop():
                return False
        elif letter in dict_valids.values():
            stack.append(letter)
    return stack == []

print(syntax_verify(sytax))