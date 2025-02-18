def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(a, s, m, e):
    return


if __name__ == '__main__':
    a1 = [11,3,7,12,15,4,8]
    merge_sort(a1, 0, len(a1)-1)
    print(a1)