def trasposto_con_lista(l_adj):
    l_res = {}
    for index in l_adj:
        l_res[index] = []
    for item in l_adj:
        for index in l_adj[item]:
            l_res[index].append(item)
    return l_res


if __name__ == '__main__':
    l_adj = {0: [1, 2], 1: [3], 2: [], 3: [2]}
    print(trasposto_con_lista(l_adj))
