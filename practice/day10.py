s = "I am Naveena"
def rev(s):
    return s[::-1]
print(rev(s))

def rev_words(s):
    split_words = s.split()
    res = []
    for word in split_words:
        res.append(word[::-1])
    result = ' '.join(res)
    return result
print(rev_words(s))

def rev_sent(s):
    split_words = s.split()[::-1]
    res = ' '.join(split_words)
    return res
print(rev_sent(s))

from collections import Counter
def first_uniq(s):
    freq = Counter(s)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(first_uniq('naveena'))

def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_ana('cat', 'tac'))

def ln_cmn_sub_str(s):
    seen = {}
    left = 0
    max_len = 0
    start = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return s[start:start+max_len]

print(ln_cmn_sub_str('abcabcdaeb'))

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
print(valid_parenthesis('{{[{}]}}'))


li1 = [1,0,2,0,3,0,4,0,6]
def fnd_rm_duplicates(li):
    uni = []
    dups = []
    for num in li:
        if num in uni:
            dups.append(num)
        else:
            uni.append(num)
    return [uni, dups]
print(fnd_rm_duplicates(li1))

def bub(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bub(li1))

def ins(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key
    return arr, arr[-2]
print(ins(li1))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print(rotate_arr(li1, 4))

def move_zeroes(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li) - len(non_zeroes))
    return non_zeroes + zeroes
print(move_zeroes(li1))

def move_zero(li):
    ins_pos = 0
    for num in li:
        if num != 0:
            li[ins_pos] = num
            ins_pos += 1

    for i in range(ins_pos, len(li)):
        li[i] = 0

    return li
print(move_zero(li1))

def find_missing(li, n):
    exp = n * (n +1) // 2
    act = sum(li)
    return exp - act
print(find_missing([1,2,4,5], 5))


def med(arr1, arr2):
    merged_arr = arr1 + arr2
    sorted_arr = sorted(merged_arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2] + sorted_arr[n//2-1]) / 2
    else:
        return sorted_arr[n//2]
    
print(med([1,2,4], [5,3,6]))

def freq_eles(li):
    res = {}
    for num in li:
        if num in res:
            res[num] += 1
        else:
            res[num] = 1
    return res

print(freq_eles(li1))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([13,20,35,46,78], 81))

def most_freq(li):
    freq = freq_eles(li)
    res = None
    max_len = 0
    for i in freq:
        if freq[i] > max_len:
            max_len =freq[i]
            res = i
    return [res, max_len]
print(most_freq(li1))

def inse(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(inse([9,3,8,2,0,7,1]))


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(100)
head.next = Node(200)
head.next.next = Node(300)

def traverse_ll(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

print(traverse_ll(head))

def rev_ll(head):
    curr = head
    prev = None
    while curr:
        new_head = curr.next
        curr.next = prev
        prev = curr
        curr = new_head
    return prev

new_head = rev_ll(head)
print(traverse_ll(new_head))

