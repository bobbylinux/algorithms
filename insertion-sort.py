def insertion_sort(numbers):
    for j in range(1, len(numbers)):
        temp = numbers[j]
        i = j - 1
        while i >= 0 and numbers[i] < temp:
            numbers[i + 1] = numbers[i]
            i -= 1
        numbers[i + 1] = temp 
    return numbers

if __name__ == '__main__':
    a = [8, 1, 9, 7, 10]
    print(a)
    print(insertion_sort(a))

