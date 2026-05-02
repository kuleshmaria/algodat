"""
P: Find strongly connected compontents (e.g. largest subsets of nodes within which all nodes are mutually reachable) using Tarjan's algorithm.
Sol: DFS with lowlinks. Nodes are put on the stack in order of discovery. Each node saves the lowest index it can go back to (low link).
     When it can't reach anything lower than itself it's the root.
Complexity: O(V+E)
"""

def tarjan(g, n):
    dfsnum = 0
    tin = [-1 for i in range(n)]     # time of discovery
    lowlink = [-1 for i in range(n)] # lowest reachable node
    st = []
    components = []

    def scc(v):
        nonlocal dfsnum, tin, lowlink, st, components

        tin[v] = dfsnum
        lowlink[v] = dfsnum
        dfsnum += 1
        st.append(v)
        for u in g[v]:
            if tin[u] == -1:
                # unvisited
                scc(u)
                lowlink[v] = min(lowlink[v], lowlink[u])
            elif tin[u] < tin[v] and u in st:
                # backedge
                lowlink[v] = min(lowlink[v], tin[u])

        if tin[v] == lowlink[v]:
            # root of scc
            sc = []
            while True:
                u = st.pop()
                sc.append(u)
                if u == v:
                    break
            components.append(sc)

    for v in range(n):
        if tin[v] == -1:
            # unvisited
            scc(v)
    print(components)

# build graph
n = 11
g = [
    [1],
    [2, 6, 8],
    [3],
    [4, 7],
    [5],
    [6],
    [2, 3],
    [6],
    [6],
    [10],
    [9]
]

tarjan(g, n)
