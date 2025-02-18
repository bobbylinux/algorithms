from collections import deque


def bfs(adj, start):
    q = deque()
    q.append(start)
    visited = set()
    while q:
        element = q.popleft()
        visited.add(element)
        for i in adj[element]:
            if i not in visited:
                q.append(i)

    return visited

if __name__ == '__main__':
    graph = {1: [2,3], 2: [1], 3: [1,4], 4:[3,5], 5:[4]}
    print(bfs(graph, 1))