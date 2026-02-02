def flatten_list(li):
    result = []
    for i in li:
        if isinstance(i, (list, tuple)):
            result.extend(flatten_list(i))
        else:
            result.append(i)

    return result


li = [1, 2, 3, 'abc', [1, 2, 3], (4, 5, 6), 'hgdhf']
print(flatten_list(li))