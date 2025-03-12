def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))

    itm = [(int(next(it)), int(next(it))) for _ in range(n)]

    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = itm[i - 1]
        for cap in range(m + 1):
            prefix[i][cap] = prefix[i - 1][cap]
            if cap >= w:
                c = prefix[i - 1][cap - w] + v
                if c > prefix[i][cap]:
                    prefix[i][cap] = c

    s = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        w, v = itm[i]
        for cap in range(m + 1):
            s[i][cap] = s[i + 1][cap]
            if cap >= w:
                c = s[i + 1][cap - w] + v
                if c > s[i][cap]:
                    s[i][cap] = c

    ans = 0
    for i in range(n):
        spec_w, spec_v = itm[i]
        best_main = 0
        for cap in range(m + 1):
            current = prefix[i][cap] + s[i + 1][m - cap]
            if current > best_main:
                best_main = current
        total = spec_v + best_main
        if total > ans:
            ans = total

    ans = max(ans, prefix[n][m])

    sys.stdout.write(str(ans))


if __name__ == '__main__':
    main()
