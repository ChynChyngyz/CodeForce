MOD = 998244353

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.insert(0, 0)
    b.insert(0, 0)

    diff = [n + 1] * (n + 2)
    diff[n] = n if a[n] != b[n] else n + 1
    for i in range(n - 1, 0, -1):
        if a[i] != b[i]:
            diff[i] = i
        else:
            diff[i] = diff[i + 1]

    freq = [0] * (n + 2)
    for i in range(1, n + 1):
        d = diff[i]
        if d <= n:
            freq[d] += 1

    H = [0] * (n + 2)
    for r in range(1, n + 1):
        H[r] = (n - r + 1) * (k - a[r]) % MOD

    R = [0] * (n + 3)
    for d in range(n, 0, -1):
        R[d] = (H[d] + R[d + 1]) % MOD

    ans = 0
    for d in range(1, n + 1):
        if a[d] < b[d]:
            F_d = ((n - d + 1) * (b[d] - a[d]) + R[d + 1]) % MOD
            ans = (ans + freq[d] * F_d) % MOD

    print(ans)

if __name__ == "__main__":
    main()
