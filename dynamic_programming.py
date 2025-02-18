def n_sum(n):
    result = [0 for _ in range(n+1)]
    result[0] = 0
    for i in range(1, n+1):
        result[i] = result[i-1] + i
    return result[n]


if __name__ == '__main__':
    print(n_sum(1))
    