s = "I am Naveena"
def rev(s):
    return s[::-1]
print(rev(s))

def rev_str(s):
    splits = s.split()[::-1]
    res = ' '.join(splits)
    return res
print(rev_str(s))

def rev_words(s):
    splits = s.split()
    res = []
    for word in splits:
        res.append(word[::-1])

    resp = ' '.join(res)
    return resp
print(rev_words(s))

from collections import Counter
def uniq(s):
    freq = Counter(s)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(uniq(s))

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
print(ln_cmn_sub_str('abcdefasb'))

def valid_parenthesis(s):
    stack = []
    pairs = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    for i in s:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)
    return not stack
print(valid_parenthesis('[{(}]'))

def rm_fnd_dups(li):
    uni = []
    dups = []
    for num in li:
        if num in uni:
            dups.append(num)
        else:
            uni.append(num)
    return [uni, dups]
print(rm_fnd_dups([1,2,2,1,2,3,4,3,5,6,4,5,7,6,7,9]))

def bub_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return [arr, arr[-2]]
print(bub_sort([6,5,7,3,8,4,1,2,9]))

def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key
    return [arr, arr[-2]]
print(ins_sort([6,5,7,3,8,4,1,2,9,11,10])) 

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print(rotate_arr([1,2,3,4], 2))

li = [1,0,2,0,3,0,4,0,5] 
def move_zeroes(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li) - len(non_zeroes))
    return non_zeroes + zeroes
print(move_zeroes(li))

def move_zero(li):
    ins_pos = 0
    for num in li:
        if num != 0:
            li[ins_pos] = num
            ins_pos += 1
            
    for i in range(ins_pos, len(li)):
        li[i] = 0

    return li
print(move_zero(li))

def find_missing(nums, n):
    exp = n * (n+1) // 2
    act = sum(nums)
    return exp - act
print(find_missing([1,2,4,5], 5))

def find_median(arr1, arr2):
    merged_arr = arr1 + arr2
    sorted_arr = sorted(merged_arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n // 2] + sorted_arr[n // 2 - 1]) / 2
    else:
        return (sorted_arr[n // 2])
print(find_median([3,1,2], [4,5,6]))

def freq_eles(li):
    freq = {}
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
print(freq_eles([1,1,1,1,2,2,3,3,3,3,3,4,4,5,5,6,7,7,7]))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([2,3,5,7], 9))

def most_freq(li):
    freq = freq_eles(li)
    res = None
    max_len = 0
    for num in freq:
        if freq[num] > max_len:
            max_len = freq[num]
            res = num
    return [res, max_len]
print(most_freq([1,1,1,1,2,2,3,3,3,3,3,4,4,5,5,6,7,7,7]))

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
        return "Queue is empty"
    
q = Queue()
print(q.queue)
for i in range(11,21):
    q.enqueue(i)

print(q.queue)
print(q.dequeue())
print(q.queue)
