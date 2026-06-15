s = 'I am Naveena'
def rev(s):
    return s[::-1]
print(rev(s))

def rev_sent(s):
    splits = s.split()[::-1]
    re = ' '.join(splits)
    return re
print(rev_sent(s))

def rev_words(s):
    splits = s.split()
    res_li = []
    for word in splits:
        res_li.append(word[::-1])
    res = ' '.join(res_li)
    return res
print(rev_words(s))

from collections import Counter
def find_uniq(s):
    freq = Counter(s)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(find_uniq(s))

def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_ana('cat', 'act'))

def str_compress(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else: 
            compressed.append(s[i-1]+str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    res = ''.join(compressed)
    return res
print(str_compress('aaabbcaaaaa'))

def ln_sub_str(s):
    seen = {}
    left = 0
    start = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return s[start:start+max_len]
print(ln_sub_str('naveena'))