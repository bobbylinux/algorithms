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
    if f[n - 1] == 0:
        f[n - 1] = memFibonacci(n - 1, f) + memFibonacci(n - 2, f)
    return f[n - 1]


def iterFibonacci(n):
    f = [0] * (n + 1)
    f[0] = 1
    f[1] = 1
    tot = 0
    for i in range(2, n + 1):
        tot = f[0] + f[1]
        f[0] = f[1]
        f[1] = tot
    return tot


def fibonacci_iterativo(n):
    f0 = 1
    f1 = 1
    tot = 0
    for i in range(2, n + 1):
        tot = f0 + f1
        f0 = f1
        f1 = tot
    return tot


def file(s, k, cap):
    if k == 0:
        return 0
    maxim = file(s, k - 1, cap)
    if s[k] <= cap:
        m = s[k] + file(s, k - 1, cap - s[k])
        if m > maxim:
            maxim = m
    return maxim

def hateville(donations):
    result = [0, donations[0]]
    for i in range(1,len(donations)):
        result.append(max(result[-1], result[-2] + donations[i]))
    return result[-1]

def ex01(points):
    result = 0
    n = len(points)
    if len(points) == 0: return 0
    if n == 1: result = points[n - 1]
    if n == 2: result = max(points[n - 1], points[n - 2])
    for x in range(2, n):
        result += max(points[x - 1], points[x - 2])
    return result


if __name__ == '__main__':
    # print(n_sum(1))
    #s = [1024, 100, 101, 2048, 1984, 55, 1, 18]
    #file(s, len(s), 5120)
    # n = 5
    # print(fibonacci(n))
    # print(memFibonacci(n, [0] * n))
    # print(iterFibonacci(n))
    # print(fibonacci_iterativo(n))
    print(hateville([0,10,5,5,8,4,7,12]))
