"""
P: 0-1 Knapsack problem: Given n items with weight w_i and value v_i,
choose a subset of items such that their total weight <= W and their total value V is maximized.
Sol: DP
Complexity: O(nW)
"""

def knapsack_01(ws, vs, W, n):
    # dp[j][i] = maximum weight <= j using up to i items
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if ws[i-1] > j:
                # item does not fit
                dp[i][j] = dp[i-1][j]
            else:
                # max of include/do not include
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - ws[i-1]] + vs[i-1])
    print(f"Max weight: {dp[n][W]}")
    return dp

knapsack_01([4, 5, 1], [1, 2, 3], 4, 3)
