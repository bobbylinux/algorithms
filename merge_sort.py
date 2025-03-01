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


if __name__ == '__main__':
    lista = [11, 3, 7, 12, 15, 4, 8]
    print(merge_sort(lista))

