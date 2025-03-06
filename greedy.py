from merge_sort import merge_sort_tuples


def coin_problem(C, up):
    counter = {x: 0 for x in C}
    while up > 0:
        upper = get_max(C, up)
        up = up - upper
        counter[upper] += 1
    return counter


def get_max(C, partial):
    upper = 0
    for x in C:
        if upper < x <= partial:
            upper = x

    return upper


def overlapped_activities(act):
    sol = []
    act = merge_sort_tuples(act, 2)
    f = 0
    for x, st, fn in act:
        if st >= f:
            sol.append((x, st, fn))
            f = fn
    return sol


def file_into_disk(files, disk_cap):
    files = merge_sort_tuples(files, 1)
    tot = 0
    sol = []
    for fn, fs in files:
        if fs + tot > disk_cap:
            break
        sol.append((fn, fs))
        tot += fs
    return sol, tot


if __name__ == '__main__':
    # print(coin_problem([1, 2, 5, 10, 20, 50], 2167))
    # act = [
    #     ('a', 0, 6),
    #     ('b', 1, 4),
    #     ('c', 3, 5),
    #     ('d', 3, 8),
    #     ('e', 4, 7),
    #     ('f', 5, 9),
    #     ('g', 6, 10),
    #     ('h', 8, 11)
    # ]
    # print(overlapped_activities(act))
    files = [
        ('a', 128),
        ('b', 1024),
        ('c', 2001),
        ('d', 166),
        ('e', 12),
        ('f', 186),
        ('g', 512)
    ]
    print(file_into_disk(files, 2048))
