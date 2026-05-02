"""
P: Check if a graph is bipartite.
Sol: BFS with alternating colors
Complexity: O(m+n)
"""

from collections import deque

def is_bipartite(g, n):
    # try to paint the graph in alternating colors
    col = [-1 for _ in range(n)]
    q = deque([])
    for i in range(n):
        if col[i] == -1:
            q.append(i)
            col[i] = 0
            while len(q) > 0:
                u = q.popleft()
                # try to paint neighbors in the other color
                for v in g[u]:
                    if col[v] == -1:
                        col[v] = 1 - col[u]
                        q.append(v)
                    elif col[v] == col[u]:
                        return False
    return True

n, m = map(int, input().split(" "))
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split(" "))
    g[u].append(v)
    g[v].append(u)
res = "attend here" if is_bipartite(g, n) else "no way"
print(res)