def main(n, s):
    d_map = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    dp = [[-float('inf')] * 4 for _ in range(n + 1)]

    for a in range(4):
        dp[0][a] = 0

    for i in range(1, n + 1):
        curr_d = d_map[s[i - 1]]
        for bef_d in range(4):
            chasy = (bef_d + 1) % 4
            Cchasy = (bef_d - 1) % 4

            dp[i][chasy] = max(dp[i][chasy], dp[i - 1][bef_d] + (1 if chasy == curr_d else 0))
            dp[i][Cchasy] = max(dp[i][Cchasy], dp[i - 1][bef_d] + (
                1 if Cchasy == curr_d else 0))

    return max(dp[n])


n = int(input())
s = input().strip()
print(main(n, s))