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
        numbers[i-1], numbers[j] = numbers[j], numbers[i-1]
        permutation_swap(numbers, i - 1)
        numbers[i-1], numbers[j] = numbers[j], numbers[i-1]


def subsets_rec(n, current, i):
    if i > n:
        # condizione di stop: ho considerato tutti gli elementi
        print(current)
        return
        # caso 1: NON includo i
    subsets_rec(n, current, i + 1)

    # caso 2: includo i
    subsets_rec(n, current + [i], i + 1)


def subsets_bitmask(n):
    for j in range(2 ** (n - 1)):
        print("{", end=" ")
        for i in range(n - 1):
            if j & 2 ** i != 0:
                print(i, ",", end=" ")
        print("}")


if __name__ == '__main__':
    # permutation_naif([1,2,3],[])
    permutation_swap([1,2,3],3)
    # subsets_rec(3, [], 1)
    # subsets_bitmask(4)
