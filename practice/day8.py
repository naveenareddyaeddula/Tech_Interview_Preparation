s1 = "i am navina"
def rev_str(s):
    return s[::-1]
print(rev_str(s1))

def rev_sent(s):
    splits = s.split()[::-1]
    res = ' '.join(splits)
    return res
print(rev_sent(s1))

def rev_words(s):
    splits = s.split()
    res_li = []
    for word in splits:
        res_li.append(word[::-1])
    res = ' '.join(res_li)
    return res
print(rev_words(s1))

def ln_cmn_substr(s):
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
print(ln_cmn_substr('abcabcabcdfab'))

from collections import Counter
def first_non_rep_ch(s):
    freq = Counter(s)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(first_non_rep_ch('naveena'))

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_anagram('god', 'dog'))

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
print(valid_parenthesis('[{()]'))

def rm_find_dups(li):
    uni = []
    dups = []
    for num in li:
        if num in uni:
            dups.append(num)
        else:
            uni.append(num)
    return [uni, dups]
print(rm_find_dups([1,2,1,1,1,2,2,1,2,3,3,3,1,3,2]))

def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bub_sort([9,3,8,2,0,7,1,6,4,5]))

def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return [arr, arr[-2]]
print(ins_sort([9,3,8,2,0,7,1,6,4,5]))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print(rotate_arr([1,2,3,4,5,6,7], 3))

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

def find_missing(arr, n):
    exp = n*(n+1) // 2
    act = sum(arr)
    return exp - act
print(find_missing([1,2,3,5], 5))

def find_median(arr1, arr2):
    sorted_arr = sorted(arr1) + sorted(arr2)
    n = len(sorted_arr)
    print(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2-1] + sorted_arr[n//2]) / 2
    else:
        return sorted_arr[n//2]
print(find_median([1,3,2,4], [7,5,6]))

def freq_eles(li):
    freq = {}
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
print(freq_eles([1,2,1,1,1,2,2,1,2,3,3,3,1,3,2]))

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
print(most_freq([1,2,1,1,1,2,2,1,2,3,3,3,1,3,2]))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([2,3,4,5,6], 10))

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(245)
head.next = Node(832)
head.next.next = Node(527)

def traversal_ll(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next
print(traversal_ll(head=head))

def new_head_ll(head):
    curr = head
    prev = None
    while curr:
        new_head = curr.next
        curr.next = prev
        prev = curr
        curr = new_head
    return prev

new_head = new_head_ll(head=head)
print(traversal_ll(head=new_head))


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