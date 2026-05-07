"""
P: Maximize the flow through a network, from source to sink, using Edmonds-Karp's algorithm.
Sol: Find a nonsaturated path from source to sink using BFS (augmenting path). Increase the flow by what is allowed by the limiting edge on the path.
Complexity: O(E*maxflow) = O(E^2V)
(O(E) - find an augmenting path, O(EV) - number of augmenting paths, since each edge can be updated at most V times)
"""

from collections import deque

def edmonds_karp(g, residual_graph, n):
    """
    residual_graph - graph with available capacities (c-f)
    """
    INF = 10**8
    max_flow = 0
    s, t = 0, n-1
    pred = [-1 for _ in range(n)]

    def find_augmenting_path():
        nonlocal pred, s, t
        vis = [False for _ in range(n)]
        q = deque([s])
        vis[s] = True
        while len(q) > 0:
            v = q.popleft()
            for u in g[v]:
                if not vis[u] and residual_graph[v][u] > 0:
                    vis[u] = True
                    pred[u] = v
                    q.append(u)
                    if u == t:
                        return True
        return False

    while find_augmenting_path():
        # find limiting edge
        curr = t
        delta_flow = INF
        while curr != s:
            prev = pred[curr]
            delta_flow = min(delta_flow, residual_graph[prev][curr])
            curr = prev
        max_flow += delta_flow

        # update residual graph
        curr = t
        while curr != s:
            prev = pred[curr]
            # forward flow
            residual_graph[prev][curr] -= delta_flow
            # allow backward flow
            residual_graph[curr][prev] += delta_flow
            curr = prev

    return max_flow


"""
input:
7 11
0 1 3
0 3 3
1 2 4
2 0 3
2 3 1
2 4 2
3 4 2
3 5 6
4 1 1
4 6 1
5 6 9

output:
5
"""

n, m = map(int, input().split(" "))
g = [[] for _ in range(n)]
capacities = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split(" "))
    g[u].append(v)
    g[v].append(u)
    capacities[u][v] = c

max_flow = edmonds_karp(g, capacities, n)
print("Max flow", max_flow)
