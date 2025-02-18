def boyer_moore(ls):
    candidate = None
    count = 0

    for el in ls:
        if count == 0:
            candidate = el
        if el == candidate:
            count += 1
        else:
            count -= 1

    count = 0
    for el in ls:
        if el == candidate:
            count += 1

    if count > len(ls) // 2:
        return True
    else:
        return False


if __name__ == '__main__':
    # print(boyer_moore([1,1,1,0,0]))
    # print(boyer_moore([1,2,3,4]))
    print( ([2,3,2,4,2,3,2,5,2]))