from time import time
def time_a_func(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"Time taken to execute {func.__name__} is {end-start:.6f} seconds")
        return res
    return wrapper

s = "I am Naveena"
def rev_str(s):
    return s[::-1]
print(rev_str(s))

def rev_sent(s):
    split_str = s.split()[::-1]
    res = ' '.join(split_str)
    return res
print(rev_sent(s))

def rev_words(s):
    split_str = s.split()
    res_li = []
    for i in split_str:
        res_li.append(i[::-1])
    res = ' '.join(res_li)
    return res
print(rev_words(s))

from collections import Counter
def uniq_char(s):
    freq = Counter(s)
    for i in freq:
        if freq[i] == 1:
            return i
print(uniq_char('navina'))

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
print(ln_cmn_sub_str('ushxuwghhsghjsg'))

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
print(valid_parenthesis('[{}]'))

li = [1,2,3,0,4,1,0,3,0,5,0,2,3]
def rm_find_dups(li):
    dups = []
    uniq = []
    for num in li:
        if num in uniq:
            dups.append(num)
        else:
            uniq.append(num)
    return [uniq, dups]
print(rm_find_dups(li))

def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return [arr, arr[-2]]
print(bub_sort(li))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print(rotate_arr(li, 3))

def move_zeroes(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li)-len(non_zeroes))
    return non_zeroes + zeroes
print(move_zeroes(li))

@time_a_func
def move_xeroes(li):
    ins_pos = 0
    for num in li:
        if num != 0:
            li[ins_pos] = num
            ins_pos += 1
    for i in range(ins_pos,len(li)):
        li[i] = 0
    return li
print(move_xeroes(li))

def find_missing(arr, n):
    exp = n * (n+1) // 2
    act = sum(arr)
    return exp - act
print(find_missing([1,2,3,4,5,6,8,9], 9))

def freq_and_most_freq(li):
    freq = {}
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_len = 0
    res = None
    for i in freq:
        if freq[i] > max_len:
            max_len = freq[i]
            res = i
    return [freq, res]
print(freq_and_most_freq(li))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum(li, 5))

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(987)
head.next = Node(988)
head.next.next = Node(999)

def traversal_ll(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next
print(traversal_ll(head))

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
print(traversal_ll(new_head))

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
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
s = Stack()
s.push(1000)
s.push(2000)
s.push(3000)
print(s.stack)
print(s.pop())
print(s.peek())

import copy
def copies(li):
    shallow_cpy = copy.copy(li)
    deep_cpy = copy.deepcopy(li)

    print(shallow_cpy)
    print(deep_cpy)

    li[0][0] = 10
    return [shallow_cpy, deep_cpy]
print(copies([[1,2],[3,4]]))

# def file_ops():
#     inp_file_path = "/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/ques.txt"
#     out_file_path = "/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/write_data.txt"
#     with open(inp_file_path, 'r') as file_data:
#         data = []
#         for line in file_data:
#             data.append(line)
    
#     with open(out_file_path, 'w') as file:
#         for line in data:
#             file.write(line)
#     return True
# print(file_ops())

def flat(li):
    res = []
    for i in li:
        if isinstance(i, (tuple, list)):
            res.extend(flat(i))
        else:
            res.append(i)
    return res
print(flat([[1,2,3],[4,5,(6,7,8,[9])]]))
    
def find_median(arr1, arr2):
    sorted_arr = sorted(arr1+arr2)
    len_sorted_arr = len(sorted_arr)

    if len_sorted_arr % 2 == 0:
        return (sorted_arr[len_sorted_arr//2-1] + sorted_arr[len_sorted_arr//2]) / 2
    else:
        return sorted_arr[len_sorted_arr//2]
    
print(find_median([1,3,4], [2,5]))
print(find_median([1,3], [2,4]))

def context_manager_without_with():
    try:
        inp_file = "/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/ques.txt"
        file = open(inp_file, 'r')
        for line in file:
            print(line)
    finally:
        file.close()
print(context_manager_without_with())


from collections import deque
class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.popleft()
        return "Queue is empty"
    
q = Queue()
print(q.queue)
for i in range(100,110):
    q.enqueue(i)
print(q.queue)
print(q.dequeue())