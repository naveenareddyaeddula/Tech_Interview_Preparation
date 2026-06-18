s1 = "I am python developer"
def rev_str(s):
    return s[::-1]
print(rev_str(s1))

def rev_words(s):
    splits = s.split()[::-1]
    res = ' '.join(splits)
    return res
print(rev_words(s1))

def rev_sen(s):
    splits = s.split()
    res_li = []
    for word in splits:
        res_li.append(word[::-1])
    res = ' '.join(res_li)
    return res
print(rev_sen(s1))

from collections import Counter
def uniq(s):
    freq = Counter(s)
    for i in freq:
        if freq[i] == 1:
            return i
print(uniq(s1))

def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_ana('god', 'dog'))

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
print(ln_cmn_sub_str('ababcabcdabcdeab'))

def valid_parenthesis(s):
    stack = []
    pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for i in s:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)
    return not stack
print(valid_parenthesis('[{)}]'))

def rm_find_dups(li):
    dups = []
    uni = []
    for num in li:
        if num in uni:
            dups.append(num)
        else:
            uni.append(num)
    return [uni, dups]
print(rm_find_dups([1,2,1,2,1,2,3,3,4,5,3,4,5]))

def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bub_sort([1,0,9,8,4,2,3]))

def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j -1

        arr[j+1] = key
    return arr

print(ins_sort([8,5,2,1,3,7]))

def sec_large(arr):
    bub = bub_sort(arr)
    ins = ins_sort(arr)
    return [bub[-2], ins[-2]]

print(sec_large([9,4,3,5,2,8,7]))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

print(rotate_arr([1,2,3,4,5,6], 3))

def move_zero(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li) - len(non_zeroes))
    return non_zeroes + zeroes
print(move_zero([1,0,2,0,3,0,4,0,5]))

def move_zeroes(li):
    ins_pos = 0
    for num in li:
        if num != 0:
            li[ins_pos] = num
            ins_pos += 1

    for i in range(ins_pos, len(li)):
        li[i] = 0

    return li
print(move_zeroes([1,0,2,0,3,0,4,0,5,0,6,0,7]))

def find_missing(arr, n):
    exp = n * (n+1) // 2
    act = sum(arr)
    return exp - act
print(find_missing([1,2,3,5], 5))

def find_median(arr1, arr2):
    merged_arr = arr1 + arr2
    sorted_arr = sorted(merged_arr)
    print(sorted_arr)
    n = len(sorted_arr)
    if n%2==0:
        return (sorted_arr[n//2-1] + sorted_arr[n//2])/2
    else:
        return sorted_arr[n//2]
    
print(find_median([1,5,4,3], [2,8,6,7]))

def freq_eles(li):
    freq = {}
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
print(freq_eles([1,1,2,3,1,5,3,2,2,4,4,2,1,2,3]))

def most_freq(li):
    freq = {}
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    res = None
    max_len = 0
    for i in freq:
        if freq[i] > max_len:
            max_len = freq[i]
            res = i
    return [res, max_len]
print(most_freq([1,1,2,3,1,5,3,2,2,4,4,2,1,2,3]))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([2,3,4,5], 6))