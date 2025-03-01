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


if __name__ == '__main__':
    print(coin_problem([1, 2, 5, 10, 20, 50], 2167))
