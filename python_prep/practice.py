def flat(li):
    res = []
    for i in li:
        if isinstance(i, (tuple, list)):
            res.extend(flat(i))
        else:
            res.append(i)

    return res

print(flat([1,2,3,[4,5,6,(1,2,3,4)]]))
        


def lon_cmn_sub_str(s):
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


print(lon_cmn_sub_str('abfvscbvbav'))



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

print(traverse_ll(head=head))

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



from collections import Counter
def uniq(s):
    freq = Counter(s)
    for i in s:
        if freq[i] == 1:
            return i
        
print(uniq('naveena'))


def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_ana('cat', 'tac'))


from time import time

def time_a_func(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"time taken to complete: {end-start:.6f}")
        return res
    return wrapper

@time_a_func
def math_eq(n1, n2):
    return n1 + n2 * n1 ** n2 / n1 * n2 /n1 * n2

print(math_eq(5,6))


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


print(two_sum([2,3,4,5,6,7], 10))