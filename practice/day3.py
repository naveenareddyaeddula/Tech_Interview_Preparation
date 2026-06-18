s = "I am Naveena"
def rev_str(s):
    return s[::-1]
print(rev_str(s))

def rev_words(s):
    split_li = s.split()[::-1]
    res = ' '.join(split_li)
    return res
print(rev_words(s))


def rev_words_sent(s):
    split_li = s.split()
    res_li = []
    for i in split_li:
        res_li.append(i[::-1])
    res = ' '.join(res_li)
    return res
print(rev_words_sent(s))

from collections import Counter
def uniq(s):
    freq = Counter(s)
    for i in freq:
        if freq[i] == 1:
            return i
print(uniq("naveena"))

def is_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_anagrams('cat', "tac"))

def longest_cmn_sub_str(s):
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
print(longest_cmn_sub_str('hjfgvdbvbvhhhcgsdh'))

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
print(valid_parenthesis('[{()}]'))


def rm_fnd_dups(li):
    uniq_li = []
    dups_li = []
    for num in li:
        if num in uniq_li:
            dups_li.append(num)
        else:
            uniq_li.append(num)
    return [uniq_li, dups_li]

print(rm_fnd_dups([1,2,1,2,2,3,4,4,5,6,7,7]))

def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return [arr, arr[-2]]
print(bub_sort([8,6,7,5,2,9,1]))

def rotate_arr(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

print(rotate_arr([4,5,6,5,4,3,2], 4))

def move_zero(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li)-len(non_zeroes))
    return non_zeroes + zeroes

print(move_zero([1,0,2,0,3,0,2]))

def move_zeroes(li):
    ins_pos = 0
    for i in li:
        if i != 0:
            li[ins_pos] = i
            ins_pos += 1
    for i in range(ins_pos, len(li)):
        li[i] = 0
    return li
print(move_zeroes([1,0,2,0,3,0,2]))

def find_missing(arr, n):
    exp = n * (n+1) // 2
    act = sum(arr)
    return exp - act
print(find_missing([1,2,3,4,5,6,7,9], 9))

def freq_ele(li):
    res = {}
    for i in li:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

print(freq_ele([1,1,1,2,2,3,4,5,4,5,6,7,8]))


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([1,2,3,4,5,6], 9))

def most_freq_ele(li):
    res = {}
    for i in li:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1

    result = None
    max_count = 0
    for i in res:
        if res[i] > max_count:
            max_count = res[i]
            result = i
    return result
print(most_freq_ele([1,1,1,2,2,3,4,5,4,5,6,7,8]))


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(5)
head.next = Node(15)
head.next.next = Node(25)

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
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
s = Stack()
s.push(100)
s.push(200)
s.push(300)
print(s.stack)
print(s.pop())
print(s.peek())


from time import time
def time_a_func(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"Time taken to comple the execution of {func.__name__} is {end-start:.6f} seconds")
        return res
    return wrapper

@time_a_func
def math_eq(a, b):
    return (a+b)**2

print(math_eq(2,3))

import copy
my_li = [[2,3], [4,5]]
shallow_cpy = copy.copy(my_li)
deep_cpy = copy.deepcopy(my_li)

print(my_li)
print(shallow_cpy)
print(deep_cpy)

my_li[0][0] = 10
print(my_li)
print(shallow_cpy)
print(deep_cpy)


# inp_file_path = "/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/ques.txt"
# out_file_path = "/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/write_data.txt"

# with open(inp_file_path, 'r') as file:
#     data = []
#     for i in file:
#         data.append(i)

# with open(out_file_path, 'w') as file:
#     for i in data:
#         file.write(i)

def flat(li):
    output = []
    for i in li:
        if isinstance(i, (tuple, list)):
            output.extend(flat(i))
        else:
            output.append(i)
    return output
print(flat([1,22,[3,[4,(5,(6,7,8))]]]))