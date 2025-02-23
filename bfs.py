from queue import Queue


def bfs_adj(adj_list, start):
    distances = [-1] * len(adj_list)
    q = Queue()
    q.put(start)  # inseriamo in coda l'elemento di partenza
    distances[start] = 0
    while not q.empty():  # mentre la coda non è vuota
        node = q.get()  # prendiamo il nodet
        # aggiunge i nodi adiacenti non visitati alla coda
        for element in adj_list[node]:  # tutti i suoi vicini
            if distances[element] == -1:
                q.put(element)
                distances[element] = distances[node] + 1
    return distances


if __name__ == '__main__':
    adj = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1, 4],
        4: [2, 3]
    }
    print(bfs_adj(adj, 0))
