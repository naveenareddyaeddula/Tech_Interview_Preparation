from collections import Counter

str1 = "I am Naveena"


def rev_str(st1):
    return st1[::-1]
print(rev_str(str1))


def rev_words(st):
    li = st.split()[::-1]
    return ' '.join(li)
print(rev_words(str1))


def rev_words_and_sen(st):
    split_li = st.split()
    li = []
    for i in split_li:
        li.append(i[::-1])
    res_str = ' '.join(li)
    return res_str
print(rev_words_and_sen(str1))


def uniq(st):
    freq = Counter(st)
    for i in freq:
        if freq[i] == 1:
            return i
print(uniq(str1))


def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_ana("dog", "god"))


def longest_uniq_sub_str(str1):
    seen = {}
    left = 0
    max_len = 0
    start = 0
    for right, ch in enumerate(str1):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left
    return str1[start:start+max_len]
print(longest_uniq_sub_str("sghdgsdb"))


def valid_parenthesis(st):
    stack = []
    pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    for i in st:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)

    return not stack
print(valid_parenthesis('{[(]}'))


def find_rm_dups(li):
    uniq = []
    dups = []
    for i in li:
        if i in uniq:
            dups.append(i)
        else:
            uniq.append(i)
    return uniq, dups
print(find_rm_dups([1, 2, 1, 2, 1, 2, 2, 3, 3, 4]))


def sort_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, arr[-2]
print(sort_arr([3,5,3,4,2,3]))


def rotate_arr(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
print(rotate_arr([1,2,3,4,5], 2))

def move_zeroes(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li) - len(non_zeroes))
    return non_zeroes + zeroes
print(move_zeroes([1,3,0,1,0,2,0,0,4])) 


def move_zero(li):
    ins_pos = 0
    for i in li:
        if i != 0:
            li[ins_pos] = i
            ins_pos += 1

    for i in range(ins_pos, len(li)):
        li[i] = 0

    return li
print(move_zero([1,3,0,1,0,2,5,0,0,4]))
     

def find_missing(nums, n):
    exp = n * (n+1) // 2
    act = sum(nums)
    return exp - act
print(find_missing([1,2,4,5], 5))


def freq_of_ele(li):
    res = {}
    for i in li:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res
print(freq_of_ele([1,2,3,1,4,2,3,1]))


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

print(two_sum([1,2,3,4], 5))


def find_most_freq_ele(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_count = 0
    res = None
    for num in freq:
        if freq[num] > max_count:
            max_count = freq[num]
            res = num

    return [res, max_count]

print(find_most_freq_ele([1,2,3,1,2,3,1,2,3,4,5,1,4]))


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(50)
head.next.next = Node(26)

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
s.push(1)
s.push(2)
s.push(3)
print(s.stack)
print(s.peek())
print(s.pop())
print(s.stack)


import copy
li = [[1, 2], [3, 4]]
shallow_li = copy.copy(li)
deep_li = copy.deepcopy(li)
print('\n')

li[0][0] = 10
print(li)
print(shallow_li)
print(deep_li)