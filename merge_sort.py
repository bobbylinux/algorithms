def merge_sort(l):
    if len(l) <= 1:
        return l
    m = len(l) // 2
    left = l[:m]
    right = l[m:]
    ll = merge_sort(left)
    lr = merge_sort(right)
    return merge(ll, lr)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    for x in left[i:]:
        result.append(x)
    for y in right[j:]:
        result.append(y)
    return result


def merge_sort_tuples(list_to_sort, index_to_sort, asc=True):
    if len(list_to_sort) <= 1:
        return list_to_sort
    m = len(list_to_sort) // 2
    left = list_to_sort[:m]
    right = list_to_sort[m:]
    ll = merge_sort(left)
    lr = merge_sort(right)
    return merge_tuples(ll, lr, index_to_sort, asc)


def merge_tuples(left, right, index_to_sort, asc=True):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if asc:
            if left[i][index_to_sort] < right[j][index_to_sort]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i][index_to_sort] > right[j][index_to_sort]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    for x in left[i:]:
        result.append(x)
    for y in right[j:]:
        result.append(y)
    return result


if __name__ == '__main__':
    lista = [11, 3, 7, 12, 15, 4, 8]
    print(merge_sort(lista))
