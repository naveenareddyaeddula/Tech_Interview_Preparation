def flat(li):
    res = []
    for i in li:
        if isinstance(i, (tuple, list)):
            res.extend(flat(i))
        else:
            res.append(i)
    return res
print(flat([1,2,3,(4,5,[6,7,8,(9)])]))


def ln_cmn_substr(st1):
    seen = {}
    left = 0
    max_len = 0
    start = 0
    for right, ch in enumerate(st1):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return st1[start:start+max_len]
print(ln_cmn_substr("hhjhedhwe"))


from collections import Counter
def first_uniq_ch(st1):
    freq = Counter(st1)
    for i in freq:
        if freq[i] == 1:
            return i
print(first_uniq_ch("naveena"))


def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)
print(is_ana("cat", "tac"))
print(is_ana("cat", "dog"))


from time import time
def time_a_func(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"Time taken to execute {func.__name__} is {end-start:.6f} seconds")
        return res
    return wrapper

@time_a_func
def math_comp(n1, n2):
    return n1 * n2 *n2 - n1+n2*n2**n1/n1**n2*n1
print(math_comp(10, 20))


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

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


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([2,3,4,5,6,7,8,9], 15))


# comprehensions for basic math calculations
li = [1,2,3,4]
squares_li = [i**2 for i in li]
print(squares_li)

inp = [1,2,3,4,5,6]
squares_di = {i:i**2 for i in inp if i % 2 == 0}
print(squares_di)


# lambda function, can have any num of argument, but can have only single expression
lambda_prac = lambda a, b: a**2 + b**2 + 2*a*b
print(lambda_prac(2,3))

#generators
def add_nums(n1,n2):
    yield n1 + n2

print(next(add_nums(2,4)))

#context managers
file_path = "/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/ques.txt"
output_file_path = "/home/naveena/Downloads/Tech_Interview_Preparation/python_prep/write_data.txt"
with open(file_path, 'r') as file_data:
    # data = file_data.read()    
    with open(output_file_path, 'w') as file:
        for data in file_data:
            file.write(data)

str_ops = "I am a python developer"
def rev_whole_str(st):
    return st[::-1]
print(rev_whole_str(str_ops))

def rev_sentence_and_words(st):
    words_li = st.split()
    res = []
    for i in words_li:
        res.append(i[::-1])
    
    res = ' '.join(res)
    return res
print(rev_sentence_and_words(str_ops))

def rev_only_words_in_a_sentence(st):
    res = st.split()[::-1]
    return ' '.join(res)
print(rev_only_words_in_a_sentence(str_ops))


def is_valid_parenthesis(str1):
    stack = []
    pairs = {'}': '{', ']': '[', ')': '('}
    for i in str1:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)
    return not stack
print(is_valid_parenthesis('[{()}]'))


dup_li = [1,1,2,2,2,3,3,3,4]
def find_rm_duplicates(li):
    duplicates = []
    uniques = []
    for i in li:
        if i not in uniques:
            uniques.append(i)
        else:
            duplicates.append(i)

    return uniques, duplicates

print(find_rm_duplicates(dup_li))


def second_highest_num_from_unsorted_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, arr[-2]

print(second_highest_num_from_unsorted_arr([1,6,5,4,3,4]))


def rotate_an_arr(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate_an_arr([1,2,3,4,5], 2))