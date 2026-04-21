s = "I am Naveena"
def rev(s):
    return s[::-1]
print(rev(s))

def rev_words(s):
    splits = s.split()
    res_li = []
    for word in splits:
        res_li.append(word[::-1])
    res = ' '.join(res_li)
    return res
print(rev_words(s))

def rev_str(s):
    splits = s.split()[::-1]
    res = ' '.join(splits)
    return res
print(rev_str(s))

from collections import Counter
def first_uniq(s):
    freq = Counter(s)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(first_uniq(s))

def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_ana('cat', 'tac'))
print(is_ana('cat', 'dog'))

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
print(ln_cmn_sub_str('ababcabcdeab'))

def valid_parenthesis(s):
    stack = []
    pairs = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    for paren in s:
        if paren in pairs:
            if not stack or stack.pop() != pairs[paren]:
                return False
        else:
            stack.append(paren)
    return not stack
print(valid_parenthesis('{[(]}'))

def rm_fnd_dups(li):
    uni = []
    dups = []
    for num in li:
        if num in uni:
            dups.append(num)
        else:
            uni.append(num)
    return [uni, dups]
print(rm_fnd_dups([1,2,1,2,3,2,4]))


li = [6,3,2,5,7,1,4]
def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return [arr, arr[-2]]
print(bub_sort(li))

def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return [arr, arr[-2]]
print(ins_sort(li))

def rotate_arr(arr, k):
    n = len(arr)
    k = k%n
    return arr[-k:] + arr[:-k]
print(rotate_arr([1,2,3,4,5,6], 2))

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
print(move_zeroes([9,0,1,0,2,0,8,0,7]))

def find_missing(nums, n):
    exp = n * (n+1) // 2
    act = sum(nums)
    return exp - act
print(find_missing([1,2,3,4,6,7], 7))

def find_median(arr1, arr2):
    comb = arr1 + arr2
    sorted_arr = sorted(comb)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2] + sorted_arr[n//2-1]) / 2
    else:
        return sorted_arr[n//2]

print(find_median((3,5), (2,1,4)))
print(find_median((4,2,1), (6,5,3)))

def freq_eles(li):
    freq = {}
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
print(freq_eles([1,1,1,2,3,2,3,4,5,6,7,6,6,6,6,7,7]))

def most_freq(li):
    freq = freq_eles(li=li)
    res = None
    max_len = 0
    for i in freq:
        if freq[i] > max_len:
            max_len = freq[i]
            res = i
    return [res, max_len]
print(most_freq([1,1,1,2,3,2,3,4,5,6,7,6,6,6,6,7,7]))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return seen[diff], i
        seen[num] = i
print(two_sum([2,3,5,7], 8))


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
        return 'Stack is empty!'
    
s = Stack()
print(s.stack)
for i in range(1, 11):
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
        return "Queue is empty!"
    
q = Queue()
print(q.queue)
for i in range(1, 11):
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
        print(f"time taken to excute {func.__name__} function is {end-start:.6f} seconds")
        return res
    return wrapper

@time_a_func
def eq(n1, n2, n3):
    return n1 + n2 * n3 *  n1
print(eq(10, 20, 30))

import copy
l1 = [[2,3], [4,5]]
shall = copy.copy(l1)
deep = copy.deepcopy(l1)

print(l1)
print(shall)
print(deep)

l1[0][0] = 1

print(l1)
print(shall)
print(deep)


def file_ops(input_file, output_file):
    with open(input_file, "r") as file:
        with open(output_file, 'w') as output_file_data:
            for row in file:
                output_file_data.write(row)
            return "Done writing data to file"

print(file_ops(input_file='/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/ques.txt',
               output_file='/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/write_data.txt'))

def flat_li(li):
    res = []
    for i in li:
        if isinstance(i, (list, tuple)):
            res.extend(flat_li(i))
        else:
            res.append(i)
    return res
print(flat_li([1,2,[3,4],(5,6)]))

def fib_memo(n, cache = {}):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    if n > 2:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
        return cache[n]

print(fib_memo(100000)) 
