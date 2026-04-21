def lm_cmn_sub_str(s):
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

print(lm_cmn_sub_str('aababsd'))


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

print(valid_parenthesis('[{()}]'))

def bub(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bub([5,3,1,4,2]))

def ins(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key

    return arr

print(ins([3,2,1,4,5]))