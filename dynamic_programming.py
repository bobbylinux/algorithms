def n_sum(n):
    result = [0 for _ in range(n + 1)]
    result[0] = 0
    for i in range(1, n + 1):
        result[i] = result[i - 1] + i
    return result[n]


def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def memFibonacci(n, f):
    if n <= 1:
        return 1
    if f[n-1] == 0:
        f[n-1] = memFibonacci(n - 1, f) + memFibonacci(n - 2, f)
    return f[n-1]


if __name__ == '__main__':
    # print(n_sum(1))
    n = 10
    print(fibonacci(n))
    print(memFibonacci(n, [0] * n))
