import heapq


# questa versione fa uso di heap, ed è la migliore scelta per grafi sparsi (complessità O[(n*m)*log(n)]
def dijkstra(l_adj, start):
    # Dizionario delle distanze con valori iniziali a +infinito
    dists = {nodo: float('inf') for nodo in l_adj}
    dists[start] = 0

    # Coda di priorità per gestire i nodi da visitare
    q = [(0, start)]  # (distanza, nodo)

    while q:
        current_dist, current_node = heapq.heappop(q)

        # Esplora i vicini
        for neighbour, weight in l_adj[current_node]:
            dist = current_dist + weight

            # Se la nuova distanza è minore o il nodo non è stato visitato, aggiorna e aggiungi alla coda
            if dist < dists[neighbour]:
                dists[neighbour] = dist
                heapq.heappush(q, (dist, neighbour))

    # Debug: stampo il dizionario prima di restituirlo
    return dists


def dijkstra_monti(adj, start):
    distances = [float('inf')] * len(adj)
    fathers = [-1] * len(adj)
    nodes = [x for x in adj]
    fathers[start] = start
    distances[start] = 0
    while nodes:
        m = float('inf')
        node = -1
        for a in nodes:
            if distances[a] < m:
                m = distances[a]
                node = a
        nodes.pop(node)
        for n, d in adj[node]:
            if distances[node] + d < distances[n]:
                fathers[n] = node
                distances[n] = distances[node] + d

    return distances


if __name__ == '__main__':
    # l_adj = {
    #     'A': [('B', 1), ('C', 4)],
    #     'B': [('A', 1), ('C', 2), ('D', 5)],
    #     'C': [('A', 4), ('B', 2), ('D', 1)],
    #     'D': [('B', 5), ('C', 1)]
    # }
    #
    # start = 'A'
    # print(dijkstra(l_adj, start))

    adj = {
        0: [(1, 4), (2, 17)],
        1: [(0, 4), (5, 1), (2, 6)],
        2: [(1, 17), (1, 6), (3, 5)],
        3: [(2, 5), (4, 10), (5, 4)],
        4: [(3, 10), (5, 12)],
        5: [(1, 1), (3, 4), (4, 12)]
    }

    print(dijkstra_monti(adj, 0))
