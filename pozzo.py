def test_pozzo_u(x, m):
    for j in range(len(m)):
        if m[x][j] == 1:  # se esiste un arco uscente da x allora non è un pozzo
            return False
    for i in range(m):
        if i != x and m[i][x] == 0:  # c'è almeno un nodo che non ha un arco entrate in x non è un pozzo universale
            return False

    return True


def pozzo_u_2(m):
    # restituisce true se il grafo m ha un pozzo universale
    for x in range(len(m)):
        if test_pozzo_u(m):
            return True
    return False


def pozzo_u_3(m):
    l = [x for x in range(len(m))]
    while len(l) > 1:
        a = l.pop()
        b = l.pop()
        if m[a][b] == 1:
            l.append(b)
        else:
            l.append(a)
    x = l.pop()
    for j in range(len(m)):
        if m[x][j] == 1:  # se esiste un arco uscente da x allora non è un pozzo
            return False
    for i in range(len(m)):
        if i != x and m[i][x] == 0:  # c'è almeno un nodo che non ha un arco entrate in x non è un pozzo universale
            return False
    return True


def pozzo_universale_adj(lad):
    n = len(lad.keys())
    candidate = None
    count = 0
    for i in range(1, n + 1):
        if len(lad[i]) == 0:
            candidate = i
            count += 1
    if count > 1 or count == 0:
        return False
    n = len(lad[candidate])
    for i in range(n):
        if candidate in lad[i]:
            return False
    return candidate


def check_pozzo_adj(u, lad):
    if len(lad[u]) == 0:
        return True
    else:
        return False


def check_pozzo_matrix(u, mat):
    n = len(mat)
    for i in range(n):
        if mat[u - 1][i] == 1:
            return False
    return True


def check_pozzo_universale_adj(u, lad):
    n = len(lad)
    if not check_pozzo_adj(u, lad):
        return False
    for i in range(1, n + 1):
        if i == u:
            continue
        if u not in lad[i]:
            return False
    return True


def check_pozzo_universale_matrix(u, mat):
    n = len(mat)
    if not check_pozzo_matrix(u, mat):
        return False
    for i in range(n):
        if i == u - 1:
            continue
        if mat[i][u - 1] == 0:
            return False
    return True


if __name__ == '__main__':
    # m = [
    #     [0, 1, 0, 0, 1],
    #     [0, 0, 1, 0, 1],
    #     [0, 0, 0, 1, 1],
    #     [1, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0]
    # ]
    # print(pozzo_u_3(m))
    lad = {1: [2, 3], 2: [3], 3: [], 4: [1, 2, 3]}
    lad2 = {1: [2, 3, 4], 2: [3, 4], 3: [], 4: []}
    mat = [[0,1,1,0], [0,0,1,0], [0,0,0,0], [1,1,1,0]]
    mat2 = [[0,1,1,1], [0,0,1,1], [0,0,0,0], [0,0,0,0]]
    # print(pozzo_universale_adj(lad))
    print(check_pozzo_universale_matrix(3, mat2))
