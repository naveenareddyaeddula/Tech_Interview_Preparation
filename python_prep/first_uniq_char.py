from collections import Counter

def first_unique_char(s):
    freq = Counter(s)

    for i in s:
        if freq[i] == 1:
            return i
        
    return None

print(first_unique_char('python'))