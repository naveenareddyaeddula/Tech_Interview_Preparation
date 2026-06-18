s1 = "I am Naveena"
def rev(s):
    return s[::-1]
print(rev(s1))

def rev_words(s):
    splits = s.split()
    res = []
    for word in splits:
        res.append(word[::-1])
    res_li = ' '.join(res)
    return res_li
print(rev_words(s1))

def rev_sent(s):
    splits = s.split()[::-1]
    res = ' '.join(splits)
    return res
print(rev_sent(s1))

from collections import Counter
def first_uniq(s):
    freq = Counter(s)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(first_uniq(s1))

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
            compressed.append(s[i-1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    res = ''.join(compressed)
    return res
print(str_compress('aaabccccddeeeee'))

def ln_cmn_sub_str(s):
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
print(ln_cmn_sub_str('fghdfhrohits'))

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
print(valid_parenthesis('{[()]}'))

def fd_rm_dups(li):
    uni = []
    dups = []
    for num in li:
        if num in uni:
            dups.append(num)
        else:
            uni.append(num)
    return [uni, dups]
print(fd_rm_dups([1,1,2,3,4,3,4,5,5,6,5,5,6]))

li = [6, 3, 2, 1, 4, 5]
def bub_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bub_sort(li))

def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return [arr, arr[-2]]
print(ins_sort(li))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print(rotate_arr([1,2,3,4,5], 2))

def move_zero(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li) - len(non_zeroes))
    return non_zeroes + zeroes
print(move_zero([1,0,2,0,3,0,4]))

def move_zeroes(li):
    ins_pos = 0
    for num in li:
        if num != 0:
            li[ins_pos] = num
            ins_pos += 1
    
    for i in range(ins_pos, len(li)):
        li[i] = 0
    return li
print(move_zeroes([1,0,2,0,3,0,4,0,5]))

def find_missing(nums, n):
    exp = n * (n+1) // 2
    act = sum(nums)
    return exp - act
print(find_missing([1,2,3,5,6], 6))

def find_median(arr1, arr2):
    merged_arr = arr1 + arr2
    sorted_arr = sorted(merged_arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n // 2] + sorted_arr[n // 2-1]) / 2
    else:
        return sorted_arr[n // 2]
print(find_median([1,3,2], [5,4,6]))
    