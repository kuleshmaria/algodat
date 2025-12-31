"""
P: Find the minimum spanning forest (union of minimum spanning trees; mst - tree with minimum weight which connects all nodes) with Kruskal's algorithm.
Sol: Sort the edges by weight and add the edge to the MSF, if no cycle is formed. Union-Find is used to check whether the addition of an edge results in a cycle.
Complexity: O(E*log(E))
"""

from collections import namedtuple

Edge = namedtuple('Edge', ['u', 'v', 'w'])

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.repr = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, a):
        if a != self.repr[a]:
            # path compression
            self.repr[a] = self.find(self.repr[a])
        return self.repr[a]

    def merge(self, a, b):
        u, v = self.find(a), self.find(b)
        if u != v:
            if self.size[v] > self.size[u]:
                # swap
                u, v = v, u
            # merge into larger set
            self.size[u] += self.size[v]
            self.repr[v] = u

    def is_same_set(self, a, b):
        return self.find(a) == self.find(b)

    def distinct_classes(self):
        return sum([1 if u == self.repr[u] else 0 for u in range(self.n)])

# build graph
n_nodes, n_edges = 5, 7
edges = [
    Edge(0, 1, 5),
    Edge(0, 3, 6),
    Edge(1, 2, 1),
    Edge(1, 3, 3),
    Edge(2, 3, 10),
    Edge(2, 4, 2),
    Edge(3, 4, 11),
    #Edge(5, 6, 11),
]

# Kruskal's algorithm
edges.sort(key=lambda e: e.w)
uf = UnionFind(n_nodes)
msf = []
min_cost = 0
for e in edges:
    if not uf.is_same_set(e.u, e.v):
        uf.merge(e.u, e.v)
        msf.append(e)
        min_cost += e.w
print(min_cost)
print(msf)
#print(uf.distinct_classes())
