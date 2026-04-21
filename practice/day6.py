s1 = "I am Naveena"
def rev_str(s):
    return s[::-1]
print(rev_str(s=s1))

def rev_words(s):
    split_words = s.split()[::-1]
    res = ' '.join(split_words)
    return res
print(rev_words(s1))

def ins_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key
    return arr
print(ins_sort([8,3,5,2, 7, 0, 1,9]))