def dfsm(u, m):
    def dfsr(u, m, visitati):
        visitati[u] = 1
        for adj in m[u]:
            if adj and not visitati[adj]:
                dfsr(adj, m, visitati)

    visitati = [0] * len(m)
    dfsr(u, m, visitati)
    return visitati


def dfsmp(u, m):
    def dfsrp(u, m, visitati, padri):
        visitati[u] = 1
        for i in range(len(m[u])):
            if m[u][i] and not visitati[i]:
                padri[i] = u
                dfsrp(i, m, visitati, padri)

    visitati = [0] * len(m)
    padri = [0] * len(m)
    padri[u] = u
    dfsrp(u, m, visitati, padri)
    return visitati, padri


def dfsl(u, l):
    def dfsr(u, l, visitati):
        visitati[u] = 1
        for v in l[u]:
            if not visitati[v]:
                dfsr(v, l, visitati)

    visitati = [0] * len(l)
    dfsr(u, l, visitati)
    return visitati

def dfs_cycle_dag(adj, start):

    def dfs_r(l, s, v):
        v[s] = 1 # nodo in esplorazione
        for x in l[s]:
            if v[x] == 0:
                if dfs_r(l, x, v):
                    return True # c'è un ciclo nel i sotto grafi
            if v[x] == 1:
                return True
        v[s] = 2 #nodo completato
        return False

    visited = [0]*len(adj)
    return dfs_r(adj, start, visited)

def dfs_cycle_nd(start, adj):
    def dfs_cycle_ndr(node, father, l_adj, visited):
        visited[node] = True
        for item in l_adj[node]:
            if item == father:
                continue
            if visited[item]:
                return True
            if dfs_cycle_ndr(item, node, l_adj, visited):
                return True
        return False

    v = [False for _ in range(len(adj))]
    return dfs_cycle_ndr(start, start, adj, v)


def dfs_cycle_dr(adj):
    def dfs_r(l, s, v):
        v[s] = 1
        for x in l[s]:
            if v[x] == 1:
                return True
            if v[x] == 0:
                if dfs_r(l, x, v): return True
        v[s] = 2
        return False

    visited = [0] * len(adj)
    return dfs_r(adj, 0, visited)


def comp_conn(lad):
    def comp_conn_r(l, y, comp_con, c_idx):
        comp_con[y] = c_idx
        for el in l[y]:
            if comp_con[el] == 0:
                comp_conn_r(l, el, comp_con, c_idx)

    cc = [0] * len(lad)
    c = 0
    for x in range(len(lad)):
        if cc[x] == 0:
            c += 1
            comp_conn_r(lad, x, cc, c)
    return cc


def path_search(destination, fathers):
    if fathers[destination] == -1:
        return []
    path = []
    while fathers[destination] != destination:
        path.append(destination)
        destination = fathers[destination]
    path.append(destination)
    path.reverse()
    return path


def coloured(l_adj):
    def dfs_r(l, s, cl, c):
        cl[s] = c
        for x in l[s]:
            if cl[x] == -1:
                dfs_r(l, x, cl, 1 - c)

    coloured = [-1] * len(l_adj)
    dfs_r(l_adj, 0, coloured, 0)
    return coloured


def time_to_visit(l_adj, start):
    time = 0

    def dfs_r(l, s, t):
        nonlocal time
        t[s] = time
        for x in l[s]:
            if t[x] == 0:
                time += 1
                dfs_r(l, x, t)

    times = [0] * len(l_adj)
    time += 1
    times[start] = time
    dfs_r(l_adj, start, times)
    return times


def bridges(l_adj):
    time = 0

    def dfs_r(l, s, tt, f, tb):
        nonlocal time
        time += 1
        ret = tt[s] = time
        for x in l[s]:
            if tt[x] == 0:
                result = dfs_r(l, x, tt, s, tb)
                if tt[s] < result:
                    tb.add((s, x))
                ret = min(ret, result)
            elif x != f:
                ret = min(tt[x], ret)
        return ret

    times = [0] * len(l_adj)
    bs = set()
    dfs_r(l_adj, 0, times, 0, bs)
    return bs


def transpose(adj):
    adj_rev = {u: [] for u in adj}
    for x in adj:
        for y in adj[x]:
            adj_rev[y].append(x)
    return adj_rev


def strongly_cc(l_adj, x):
    tr_adj = transpose(l_adj)
    visited = dfsl(l_adj, x)
    visited_tr = dfsl(tr_adj, x)
    result = [0] * len(l_adj)


def intersection(v1, v2):
    vtot = [0] * len(v1)
    if len(v1) != len(v2):
        return vtot
    for x in range(len(v1)):
        if v1[x] == v2[x]:
            vtot.append(v1[x])
    return vtot


def dfs_dir(G):
    def dfs_r(l, x, tt, ff, vv):

        nonlocal c
        nonlocal te
        nonlocal be
        nonlocal ae
        nonlocal fe
        c += 1
        tt[x] = c
        vv[x] = 1
        for y in l[x]:
            if vv[y] == 0:
                te += 1
                ff[y] = x
                dfs_r(l, y, tt, ff, vv)
            else:
                if tt[x] < tt[y]:
                    fe += 1
                else:
                    if vv[y] == 1:
                        be += 1
                    else:
                        ae += 1
        vv[x] = 2

    te = 0
    fe = 0
    be = 0
    ae = 0
    c = 0
    times = []
    visited = [0] * len(G)
    fathers = [-1] * len(G)
    fathers[0] = 0
    dfs_r(G, 0, times, fathers, visited)
    return te, fe, be, ae


def set_id(l_adj):
    def dfs_r(l, s, tt):
        nonlocal time
        time += 1
        tt[s] = time
        for x in l[s]:
            if tt[x] == -1:
                dfs_r(l, x, tt)

    times = [-1] * len(l_adj)
    time = 0
    times[0] = 0
    dfs_r(l_adj, 0, times)
    return times


def topol_ord(l_adj):
    def dfsr(u, l, v, st):
        v[u] = 1
        for x in l[u]:
            if not v[x]:
                dfsr(x, l, v, st)
        st.append(u)

    st = []
    visited = [0] * len(l_adj)
    dfsr(0, l_adj, visited, st)
    result = []
    while st:
        result.append(st.pop())
    return result


def tarjan_scc(l_adj):
    def dfs_r(l, s, tt, low, stack, on_stack, scc_list):
        nonlocal time
        time += 1
        tt[s] = low[s] = time  # Assegna l'indice di visita e il valore minimo raggiungibile
        stack.append(s)
        on_stack[s] = True

        for x in l[s]:
            if tt[x] == -1:  # Se il nodo non è stato visitato
                dfs_r(l, x, tt, low, stack, on_stack, scc_list)
                low[s] = min(low[s], low[x])  # Aggiorna il valore minimo raggiungibile
            elif on_stack[x]:  # Se il nodo è nello stack, è parte della stessa SCC
                low[s] = min(low[s], tt[x])

        # Se s è la radice di una SCC, estrai i nodi fino a s
        if tt[s] == low[s]:
            scc = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                scc.append(node)
                if node == s:
                    break
            scc_list.append(scc)  # Aggiungi la SCC trovata

    n = len(l_adj)
    times = [-1] * n  # Indici di visita
    low = [-1] * n  # Valori low-link
    stack = []  # Stack per tenere traccia dei nodi della SCC
    on_stack = [False] * n  # Indica se un nodo è nello stack
    scc_list = []  # Lista delle SCC
    time = 0

    for i in range(n):  # Se il grafo non è connesso, avvia DFS per ogni nodo non visitato
        if times[i] == -1:
            dfs_r(l_adj, i, times, low, stack, on_stack, scc_list)

    return scc_list  # Restituisce le componenti fortemente connesse


if __name__ == '__main__':
    # m = [[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0],
    #      [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0]]
    # l = {0: [1, 2], 1: [0], 2: [0, 3, 4], 3: [2, 5], 4: [2, 5], 5: [3, 4]}
    # v, f = (dfslp(0, l))
    # print(path_search(4, f))
    # l1 = [[1],[0,3],[3],[1,2]]
    # l2 = [[1,2],[],[1]]
    # Nil, padri = dfslp(1, l)
    # print(padri)
    # l3 = {0: [1, 5], 1: [0, 5], 2: [4], 3: [], 4: [2], 5: [0, 1]}
    # print(comp_conn(l3))
    # l_c = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]}
    # l_adj = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6]}
    # print(dfs_cycle_nd(0, l_c))
    # print(coloured(l_adj))
    # l_adj = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [4, 6]}
    # print(bridges(l_adj))
    # print(time_to_visit(l_adj, 0))
    # G = {0: [1], 1: [5, 7], 2: [0, 1, 6], 3: [4, 6], 4: [1], 5: [], 6: [2], 7: [0]}
    # print(transpose(G))
    # print(intersection([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]))
    # g = {0: [1], 1: [2, 3, 4], 2: [0, 3], 3: [5], 4: [6], 5: [3, 4, 6], 6: [4]}
    # print(set_id(g))
    # g = {0: [1], 1: [2, 3], 2: [4], 3: [], 4: [5, 6], 5: [], 6: []}
    # print(topol_ord(g))
    g = {0: [1, 3], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}
    print(tarjan_scc(g))
