s1 = "I am Naveena"
print(s1)

def rev(s):
    return s[::-1]
print(rev(s1))

def rev_words(s):
    splits = s.split()
    res = []
    for word in splits:
        res.append(word[::-1])
    resp = ' '.join(res)
    return resp
print(rev_words(s1))

def rev_sen(s):
    splits = s.split()[::-1]
    res = ' '.join(splits)
    return res
print(rev_sen(s1))

from collections import Counter
def first_uniq(s):
    freq = Counter(s)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(first_uniq(s1))

def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_ana('cat', 'tac'))

def str_compress(s):
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
print(str_compress('aaabbbbcdaaaaa'))

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
print(ln_sub_str('sddsjsdjjknhbskl'))

def valid_parenthesis(s):
    stack = []
    pairs = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    for i in s:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)

    return not stack
print(valid_parenthesis('[{()}]'))


li1 = [1,1,1,2,2,3,3,4,5]
def rm_fd_dups(li):
    uni = []
    dups = []
    for num in li:
        if num in uni:
            dups.append(num)
        else:
            uni.append(num)
    return [uni, dups]
print(rm_fd_dups(li1))

def bub(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return [arr, arr[-2]]
print(bub([6,5,3,5,4,1,2]))

def ins(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return [arr, arr[-2]]
print(ins([6,5,3,5,4,1,2,1]))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print(rotate_arr([1,2,3,4,5], 3))

