words = ["listen", "silent", "enlist", "rat", "tar", "god", "dog", "evil", "vile", "veil", "cat"]

def anagram_maker(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams: anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())
print(anagram_maker(words))