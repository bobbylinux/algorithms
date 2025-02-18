def is_a_and_b_set(s, subsets):
    subsets_seen = []
    for a in subsets:
        b = s - a
        if b in subsets_seen:
            return a, b
        subsets_seen.append(a)
    return False


if __name__ == '__main__':
    s = {1, 2, 3, 4}
    subsets = [{1, 2, 3}, {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 3}]
    print(is_a_and_b_set(s, subsets))
