"""
P: Find the longest common subsequence between 2 sequences of length n and m.
A subsequence is obtained by removing none or a x items without changing the order of the remaining ones.
Sol: DP
Complexity: O(n*m)
"""

s1 = "ACGGTGTCGTGCTATGCTGATGCTGACTTATATGCTA"
s2 = "CGTTCGGCTATCGTACGTTCTATTCTATGATTTCTAA"

n, m = len(s1), len(s2)
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(f"Sequence A: {s1}\nSequence B: {s2}")
print(f"Length of LCS: {dp[n][m]}")

# backtracking
lcs = ""
i, j = n, m
while i != 0 and j!= 0:
    if s1[i-1] == s2[j-1]:
        lcs = s1[i-1] + lcs
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1

print(f"LCS: {lcs}")
