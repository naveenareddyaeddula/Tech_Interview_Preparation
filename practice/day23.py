def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())
print(group_anagrams(['cat', 'act', 'god', 'odg']))

def flat(li):
    res = []
    for i in li:
        if isinstance(i, (list, tuple)):
            res.extend(flat(i))
        else:
            res.append(i)
    return res
print(flat([[1,2,3],[4,5,(6,7,8,[9])]]))

def sort_by_values(d1):
    return dict(sorted(d1.items(), key=lambda item:item[1]))
d = {"a": 10, "b": 2, "c": 3}
print(sort_by_values(d))