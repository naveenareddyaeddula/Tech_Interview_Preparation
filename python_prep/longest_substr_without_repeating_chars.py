def longest_unique_substr(s):
    seen = {}
    start = 0
    max_len = 0
    left = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return s[start:start + max_len]


s = 'abcababcabcd'
print(longest_unique_substr(s))