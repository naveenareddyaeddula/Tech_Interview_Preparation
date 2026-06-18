s = "I am Naveena"
def rev(s):
    return s[::-1]
print(rev(s))

def rev_words(s):
    splits = s.split()[::-1]
    res = ' '.join(splits)
    return res
print(rev_words(s))

def rev_sent(s):
    splits = s.split()
    res_li = []
    for word in splits:
        res_li.append(word[::-1])
    res = ' '.join(res_li)
    return res
print(rev_sent(s))

from collections import Counter
def first_uniq(s):
    freq = Counter(s)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(first_uniq(s))

def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_ana('cat', 'act'))

def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())
print(group_anagrams(['cat', 'dog', 'act', 'god', 'tac']))

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
print(str_compress('aaabccaaaaa'))

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
    return [s[start:start+max_len], len(s[start:start+max_len])]
print(ln_cmn_sub_str('abcdefabcbb'))

def valid_parenthesis(s):
    stack = []
    pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    for i in s:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)
    return not stack
print(valid_parenthesis('[{()}]'))

def rm_fd_dups(li):
    uni = []
    dups = []
    for num in li:
        if num in uni:
            dups.append(num)
        else:
            uni.append(num)
    return [uni, dups]
print(rm_fd_dups([1,1,1,2,2,3,3,3,3]))

def bub_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr, arr[-2])

li1 = [5,3,4,1,2]
print(bub_sort(li1))

def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return [arr, arr[-2]]
print(ins_sort(li1))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print(rotate_arr([1,2,3,4,5,6], 2))

li2 = [1,0,2,0,3,0,4]
def move_zero(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li) - len(non_zeroes))
    return non_zeroes + zeroes
print(move_zero(li2))

def move_zeroes(li):
    ins_pos = 0
    for num in li:
        if num != 0:
            li[ins_pos] = num
            ins_pos += 1
    for i in range(ins_pos, len(li)):
        li[i] = 0
    
    return li
print(move_zeroes(li2))

def find_missing(nums, n):
    exp = n * (n+1) // 2
    act = sum(nums)
    return exp - act

print(find_missing([1,2,3,5], 5))

def find_median(arr1, arr2):
    merged_arr = arr1 + arr2
    sorted_arr = sorted(merged_arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2] + sorted_arr[n//2-1]) / 2
    else:
        return sorted_arr[n//2]
print(find_median([1,4,2], [5,3,6]))


li3 = [1,1,1,2,2,3,3,3,3]
def freq_eles(li):
    freq = {}
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
print(freq_eles(li3))

def most_freq(li):
    freq = freq_eles(li)
    max_len = 0
    res = None
    for num in freq:
        if freq[num] > max_len:
            max_len = freq[num]
            res = num
    return {res: max_len}
print(most_freq(li3))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([2,3,4,5], 7))

d1 = {'a': 10, 'b':2, 'c':3}
d2 = {'b': 2, 'c': 5, 'd': 6}
def common_keys(d1, d2):
    return list(sorted(d1.keys() & d2.keys()))
print(common_keys(d1, d2))

def sort_by_values(d1):
    return dict(sorted(d1.items(), key=lambda item:item[1]))
print(sort_by_values(d1))

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(200)
head.next = Node(300)
head.next.next = Node(400)

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

class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return 'Stack is empty'

s = Stack()
print(s.stack)

for i in range(1,11):
    s.push(i)

print(s.stack)
print(s.pop())
print(s.stack)

from collections import deque
class Queue():
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return 'Queue is empty'
    
q = Queue()
print(q.queue)
for i in range(11, 21):
    q.enqueue(i)
print(q.queue)
print(q.dequeue())
print(q.queue)


import time
def time_a_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken to complete the execution is {end-start:.6f} seconds")
        return res
    return wrapper


@time_a_func
def math_eq(n1, n2):
    return n1 * n2 ** n1 * n2
print(math_eq(10, 20))