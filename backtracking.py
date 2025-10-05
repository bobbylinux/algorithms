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
    if i == len(numbers):
        print(numbers)
        return

    for j in range(i, len(numbers)):
        numbers[i], numbers[j] = numbers[j], numbers[i]
        permutation_swap(numbers, i+1)
        numbers[i], numbers[j] = numbers[j], numbers[i]

def subsets_rec(n, current, i):
    if i > n:
        # condizione di stop: ho considerato tutti gli elementi
        print(current)
        return 
    # caso 1: NON includo i
    subsets_rec(n, current, i+1)

    # caso 2: includo i
    subsets_rec(n, current + [i], i+1)


if __name__ == '__main__':
    # permutation_naif([1,2,3],[])
    #permutation_swap([1,2,3],0)
    subsets_rec(3, [], 1)
