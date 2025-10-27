def permutation_naif(numbers, partials):
    if len(numbers) == len(partials):
        print(partials)
        return

    for num in numbers:
        if num not in partials:
            partials.append(num)
            permutation_naif(numbers, partials)
            partials.pop()


def permutation_swap(numbers, i):
    if i == 0:
        print(numbers)
        return

    for j in range(i):
        numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]
        permutation_swap(numbers, i - 1)
        numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]


def subsets_rec(n, current, i):
    if i > n:
        # condizione di stop: ho considerato tutti gli elementi
        print(current)
        return
        # caso 1: NON includo i
    subsets_rec(n, current, i + 1)

    # caso 2: includo i
    subsets_rec(n, current + [i], i + 1)


def subsets_naif(n, current, i):
    if i > n:
        print(current)
        return
    subsets_naif(n, current, i + 1)
    subsets_naif(n, current + [i], i + 1)


def subsets_k_of_n(n, missing, current, i):
    if missing == 0:
        print(current)
        return
    # se non ho superato n e missing è maggiore di zero e minore delle scelte ancora da fare
    elif i <= n and 0 < missing <= n - (i - 1):
        subsets_k_of_n(n, missing, current, i + 1)
        subsets_k_of_n(n, missing - 1, current + [i], i + 1)


def subsets_bitmask(n):
    for j in range(2 ** (n - 1)):
        print("{", end=" ")
        for i in range(n - 1):
            if j & 2 ** i != 0:
                print(i, ",", end=" ")
        print("}")


def ex03_0925(n, s):
    if len(s) == n:
        print(s)
    for j in (0, 1, 2):
        if len(s) < 1 or (len(s) == 1 and s[0] + j >= 2) or (len(s) >= 2 and 4 <= j + s[-1] + s[-2] <= 5):
            s.append(j)
            ex03_0925(n, s)
            s.pop()


def ex03_0724(n, i, s, pb, cb):
    if n == i:
        print(s)
        return
    for x in {0, 1}:
        if cb is None:
            cb = {"k": x, "v": 1}
            s.append(x)
            ex03_0724(n, i + 1, s, pb, cb)
            s.pop(x)
        else:
            if x == cb["k"]:
                cb["v"] += cb["v"] + 1
                s.append(x)
                ex03_0724(n, i + 1, s, pb, cb)
                s.pop(x)
            else:
                pb = cb
                cb = {"k": x, "v": 1}
                s.append(x)
                ex03_0724(n, i + 1, s, pb, cb)
                s.pop(x)
        if pb is not None and cb is not None and cb["v"] <= pb["v"]:
            s.append(x)
            ex03_0724(n, i + 1, s, pb, cb)
            s.pop(x)


if __name__ == '__main__':
    # permutation_naif([1,2,3],[])
    # permutation_swap(['A', 'B', 'C'], 3)
    # subsets_rec(3, [], 1)
    # subsets_k_of_n(6, 3,[], 1)
    # subsets_naif(3,[], 1)
    # subsets_bitmask(4)
    # c = ex03_0925(5, [])
    ex03_0724(4, 0, [], None, None)
