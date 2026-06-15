def str_compress(s):
    if not s:
        return None
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    res = ''.join(compressed)
    return res
print(str_compress('aabcccccaaa'))

d1 = {'a': 10, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 3, 'd': 4}
def cmn_keys(d1, d2):
    return d1.keys() & d2.keys()
print(cmn_keys(d1, d2))

def sort_by_values(d1):
    return dict(sorted(d1.items(), key=lambda item:item[1]))
print(sort_by_values(d1))

def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())
print(group_anagrams(['cat', 'god', 'dog', 'act', 'tac']))