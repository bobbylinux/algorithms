import heapq


def prim(adj, start):
    mst = []  # Lista per gli archi dell'albero ricoprente minimo
    visited = [False] * len(adj)  # Lista per tenere traccia dei nodi visitati
    node_index = {node: i for i, node in enumerate(adj.keys())}  # Mappiamo i nodi agli indici
    min_heap = [(0, start, None)]  # Heap con (peso, nodo, nodo precedente)

    while min_heap:
        cost, node, prev = heapq.heappop(min_heap)

        if visited[node_index[node]]:
            continue

        visited[node_index[node]] = True
        if prev is not None:
            mst.append((prev, node, cost))

        for neighbor, weight in adj[node]:
            if not visited[node_index[neighbor]]:
                heapq.heappush(min_heap, (weight, neighbor, node))

    return mst


# Esempio di utilizzo
adj = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

mst = prim(adj, 'A')
print("Albero Ricoprente Minimo:", mst)
