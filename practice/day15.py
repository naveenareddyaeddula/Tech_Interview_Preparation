d1 = {'a': 10, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 3, 'd': 4}

def common_keys(d1, d2):
    return list(d1.keys() & d2.keys())
print(common_keys(d1, d2))

def sort_by_values(d1):
    return dict(sorted(d1.items(), key=lambda item:item[1]))
print(sort_by_values(d1))

words = ['cat', 'god', 'dog', 'act', 'tac']
def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())
print(group_anagrams(words))
    
def compressed_str(str1):
    if not str1:
        return None
    
    compressed = []
    count = 1
    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            compressed.append(str1[i-1] + str(count))
            count = 1

    compressed.append(str1[-1] + str(count))
    res = ''.join(compressed)
    return res

print(compressed_str('aabcccccaaa'))  # a2b1c5a3