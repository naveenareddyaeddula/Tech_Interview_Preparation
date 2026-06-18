st = "I am Naveena"
def rev(st):
    return st[::-1]
print(rev(st))

def rev_words(st):
    split_li = st.split()[::-1]
    res = ' '.join(split_li)
    return res
print(rev_words(st))

def rev_sente(st):
    split_li = st.split()
    res_li = []
    for word in split_li:
        res_li.append(word[::-1])
    res = ' '.join(res_li)
    return res
print(rev_sente(st))

from collections import Counter
def first_uniq(st):
    freq = Counter(st)
    for ch in freq:
        if freq[ch] == 1:
            return ch
print(first_uniq('naveena'))

def is_anas(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_anas("cat", "tac"))

def find_ln_cmn_sub_str(st):
    seen = {}
    left = 0
    max_len = 0
    start = 0
    for right, ch in enumerate(st):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left
    return st[start:start+max_len]
print(find_ln_cmn_sub_str('ghfhghhjbnm'))

def valid_parenthesis(st):
    stack = []
    pairs = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    for i in st:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)
    return not stack
print(valid_parenthesis('[({)]'))

def rm_find_dups(li):
    dups_li = []
    uniq_li = []
    for num in li:
        if num in uniq_li:
            dups_li.append(num)
        else:
            uniq_li.append(num)
    return [uniq_li, dups_li]
print(rm_find_dups([1,1,2,2,1,2,3,4,5,6,7,5,4,3,2]))

def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    return [arr, arr[-2]]
print(bub_sort([1,1,2,2,1,2,3,4,5,6,7,5,4,3,2]))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print(rotate_arr([1,2,3,4,5,6,7], 3))

def move_zeroes_li_comp(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li) - len(non_zeroes))
    return non_zeroes + zeroes
print(move_zeroes_li_comp([1,0,2,0,3,0,4,0,5]))

def move_zeros_by_pos(li):
    ins_pos = 0
    for num in li:
        if num != 0:
            li[ins_pos] = num
            ins_pos += 1
    for i in range(ins_pos, len(li)):
        li[i] = 0
    return li
print(move_zeros_by_pos([1,0,2,0,3,0,4,0,5,0,6]))

def find_missing(nums, n):
    exp = n * (n+1) // 2
    act = sum(nums)
    return exp - act
print(find_missing([1,2,3,4,5,7,8], 8))

def median_of_sorted_arr(arr1, arr2):
    sorted_arr = sorted(arr1) + sorted(arr2)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n//2-1] + sorted_arr[n//2]) / 2
    else:
        return sorted_arr[n//2]
print(median_of_sorted_arr([1,2,3,4], [5,6,7,8,9]))

def freq_of_ele(li):
    res = {}
    for num in li:
        if num in res:
            res[num] += 1
        else:
            res[num] = 1
    return res
print(freq_of_ele([1,1,2,2,1,2,3,4,5,6,7,5,4,3,2]))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([1,2,3,4,5,6,7], 5))

def find_most_freq_ele(li):
    res_li = freq_of_ele(li)
    res = None
    max_count = 0
    for i in res_li:
        if res_li[i] > max_count:
            max_count = res_li[i]
            res = i
    return {res: max_count}
print(find_most_freq_ele([1,1,2,2,1,2,3,4,5,6,7,5,4,3,2]))

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(100)
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)

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

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "The stack is empty"
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "The stack is empty"
    
s = Stack()
print(s.stack)
for i in range(0, 11):
    s.push(i)
print(s.stack)
print(s.peek())
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
print('\n')
print(q.queue)
for i in range(1, 11):
    q.enqueue(i)
print(q.queue)
print(q.dequeue())
print(q.queue)