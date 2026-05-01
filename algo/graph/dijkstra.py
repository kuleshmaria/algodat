"""
P: Find the shortest path from the start node to any other node using Dijkstra's algorithm (requires non-negative edges).
Sol: Choose the node with the shortest distance from the origin and that hasn't been visited. Update its neighbors.
Complexity: O(E*log(V)) provided we use a priority queue
"""

import heapq

def dijkstra(g, n, s = 0):
    INF = 10**10
    dist = [INF for _ in range(n)]
    # priority queue: (distance from origin, node)
    q = []
    # start node
    dist[s] = 0
    heapq.heappush(q, (0, s))

    while len(q) > 0:
        # choose the node closest to origin
        d, v = heapq.heappop(q)
        # ignore old value
        if d != dist[v]:
            continue
        # update neighbors
        for (u, w) in g[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                heapq.heappush(q, (dist[u], u))
    return dist

# build graph
n = 4
g = [[] for _ in range(n)]
g[0].append((1, 2))
g[1].append((2, 2))
g[3].append((0, 2))

dist = dijkstra(g, n)
print(dist)
