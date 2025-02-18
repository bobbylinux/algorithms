import heapq


def dijkstra(l_adj, start):
    # Dizionario delle distanze con valori iniziali a +infinito
    distanze = {nodo: float('inf') for nodo in l_adj}
    distanze[start] = 0

    # Coda di priorità per gestire i nodi da visitare
    coda = [(0, start)]  # (distanza, nodo)

    while coda:
        distanza_corrente, nodo_corrente = heapq.heappop(coda)

        # Esplora i vicini
        for vicino, peso in l_adj[nodo_corrente]:
            distanza = distanza_corrente + peso

            # Se la nuova distanza è minore o il nodo non è stato visitato, aggiorna e aggiungi alla coda
            if distanza < distanze[vicino]:
                distanze[vicino] = distanza
                heapq.heappush(coda, (distanza, vicino))

    # Debug: stampo il dizionario prima di restituirlo
    return distanze




if __name__ == '__main__':
    l_adj = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start = 'A'
    print(dijkstra(l_adj, start))