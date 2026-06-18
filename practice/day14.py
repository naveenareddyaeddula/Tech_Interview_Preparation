def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())
print(group_anagrams(["eat", "tea", "ate", "bat", "tab"]))

def cmn_keys(d1, d2):
    return list(sorted(d1.keys() & d2.keys()))

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}
print(cmn_keys(d1, d2))

def sort_by_values(d):
    return dict(sorted(d.items(), key=lambda item:item[1]))
d = {"a": 10, "b": 2, "c": 3}
print(sort_by_values(d))
