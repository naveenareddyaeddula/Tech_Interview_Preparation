def flatten_li(li):
    res = []
    for i in li:
        if isinstance(i, (tuple,list)):
            res.extend(flatten_li(i))
        else:
            res.append(i)
    return res

li = [[[5, 6], [7, 8]], [9], [3, 4, 7]]
print(flatten_li(li))


def lon_cmn_sub_str(st):
    seen = {}
    left = 0
    start = 0
    max_len = 0
    for right, ch in enumerate(st):
        if ch in seen and seen[ch]>=left:
            left = seen[ch] + 1

        seen[ch] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return st[start:start+max_len]

print(lon_cmn_sub_str('abvfscvasg'))


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

print(two_sum([2,3,4,5], 7))


str1 = "I am Naveena"
def rev_(st):
    return st[::-1]

print(rev_(str1))

# Naveena am I
split_str = str1.split()[::-1]
split_str = ' '.join(split_str)
print(split_str)

split_li = str1.split()
new_li = []
for i in split_li:
    new_li.append(i[::-1])

res_str = ' '.join(new_li)
print(res_str)


def is_valid(st):
    stack = []
    pairs = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for i in st:
        if i in pairs:
            if not stack or stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)

    return not stack

print(is_valid('{[(])}'))



def sort_ar(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr, arr[-2]

print(sort_ar([1,6,5,3,2,4]))


def rotate_arr(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

print(rotate_arr([1,2,3,4,5,6], 3))


def move_zeroes(li):
    non_zeroes = [num for num in li if num != 0]
    zeroes = [0] * (len(li) - len(non_zeroes))
    return non_zeroes + zeroes

print(move_zeroes([1,2,0,3,0,4]))

def move_zero(li):
    insert_pos = 0
    for i in li:
        if i != 0:
            li[insert_pos] = i
            insert_pos += 1

    for i in range(insert_pos, len(li)):
        li[i] = 0

    return li

print(move_zero([1,2,0,3,0,4]))


def find_missing(nums, n):
    exp = n * (n+1) // 2
    act = sum(nums)
    return exp - act

print(find_missing([1,2,3,4,5,6,8,9], 9))


def find_most_freq(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_count = 0
    res = None
    for i in freq:
        if freq[i] > max_count:
            max_count = freq[i]
            res = num

    return {res: max_count}

print(find_most_freq([1,2,2,1,2,3,4,2,1,4,4, 1,1]))


class Stack():
    def __init__(self):
        self.stack = []

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
    
    def is_empty(self):
        return len(self.stack) == 0
    

s = Stack()
s.push(15)
s.push(25)
s.push(35)
print(s.stack)
print(s.peek())
print(s.pop())
print(s.stack)


def find_median(arr1, arr2):
    sorted_arr = sorted(arr1 + arr2)
    n = len(sorted_arr)
    if n % 2 == 0:
        return (sorted_arr[n // 2-1] + sorted_arr[n // 2]) / 2
    else:
        return sorted_arr[n // 2]
    
print(find_median([1,3,4], [2,5,6]))

