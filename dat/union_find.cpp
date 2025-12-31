#include <iostream>
#include <vector>

/**
 * Union-Find implementation in C++.
 * Operations: find, union
 */

class UnionFind
{
    std::vector<int> repr;
    std::vector<int> size;

    public:
        UnionFind(int n) : repr(n), size(n, 1)
        {
            for(int i = 0; i < n; i++)
            {
                repr[i] = i;
            }
        }

        int find(int a)
        {
            // find set representative
            if(repr[a] != a)
            {
                // path compression
                return repr[a] = find(repr[a]);
            }
            return repr[a];
        }

        void merge(int a, int b)
        {
            // combine sets
            int u = find(a);
            int v = find(b);

            if(u != v)
            {
                // union by size
                if(size[v] > size[u])
                {
                    std::swap(u, v);
                }
                // merge into larger set
                repr[v] = u;
                size[u] += size[v];
            }
        }

        bool is_same_set(int a, int b)
        {
            return find(a) == find(b);
        }
};

int main()
{
    int n = 3;
    UnionFind uf(n);
    uf.merge(1, 2);
    std::cout << (uf.is_same_set(1,2))<<"\n";
    std::cout << (uf.is_same_set(3,2))<<"\n";
    std::cout << (uf.is_same_set(2,2))<<"\n";
    return 0;
}
