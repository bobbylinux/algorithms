from deque import Deque

def bfs_adj(adj_list, start, target):
    visited = set()
    q = Deque()
    q.push(start) #inseriamo in coda l'elemento di partenza

    while not q.empty(): #mentre la coda non è vuota
        node = q.pop() #prendiamo il node
        if node == target:  # Controlla se il nodo corrente è il target
            return target
        if node in visited:
            continue
        visited.add(node)
        # aggiunge i nodi adiacenti non visitati alla coda
        for element in adj_list[node]: #tutti i suoi vicini
             if element not in visited:
                q.push(element)
    return None


def connected_components(adj, start):
    return False


if __name__ == '__main__':
    adj = {
        1: [2,3],
        2: [1,4],
        3: [1,5],
        4: [2,5],
        5: [3,4]
    }
    print(bfs_adj(adj, 1,5))
