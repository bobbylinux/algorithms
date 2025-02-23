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




if __name__ == '__main__':
    l_adj = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start = 'A'
    print(dijkstra(l_adj, start))