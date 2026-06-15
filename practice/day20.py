import time

def time_a_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken to execute {func.__name__} is {end-start:.6f} seconds")
        return res
    return wrapper

@time_a_function
def math_eq(n1, n2, n3):
    return n1 * n2 ** n2 * n3 * n1

print(math_eq(10, 20, 30))

import copy
original = [[1,2], [3,4]]
print(original)
deep_cpy = copy.deepcopy(original)
print(deep_cpy)
shallow_cpy = copy.copy(original)
print(shallow_cpy)

original[0][0] = 10
print(original)
print(shallow_cpy)
print(deep_cpy)

input_file = '/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/ques.txt'
output_file = '/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/write_data.txt'
def file_ops(input_file, output_file):
    try:
        with open(input_file, 'r') as input_data:
            data = input_data.read()

        with open(output_file, 'w+') as output_data:
            for row in data:
                output_data.write(row)

        return True
    except Exception as e:
        return str(e)
print(file_ops(input_file, output_file))

def flat(li):
    res = []
    for i in li:
        if isinstance(i, (tuple, list)):
            res.extend(flat(i))
        else:
            res.append(i)
    return res
print(flat([1,2,[3,4,5], [6,(7,8, (9))]])) 

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

for i in range(11,21):
    q.enqueue(i)

print(q.queue)
print(q.dequeue())
print(q.queue)

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1000)
head.next = Node(2000)
head.next.next = Node(3000)

def traverse_ll(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

print(traverse_ll(head))

def reverse_ll(head):
    curr = head
    prev = None
    while curr:
        new_head = curr.next
        curr.next = prev
        prev = curr
        curr = new_head
    return prev

new_head = reverse_ll(head)
print(traverse_ll(new_head))

def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())
print(group_anagrams(['cat', 'dog', 'act', 'tac', 'god']))


d1 = {'a': 10, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c':5, 'd': 6}
def sort_by_values(d1):
    return dict(sorted(d1.items(), key=lambda item:item[1]))
print(sort_by_values(d1))

def common_keys(d1, d2):
    return d1.keys() & d2.keys()
print(common_keys(d1, d2))

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([2,3,4,5], 9))

li1 = [1,1,1,2,2,1,2,1,2,3,4,3,4,3,3,3,3]
def freq_eles(li):
    freq = {}
    for num in li:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
print(freq_eles(li1))


