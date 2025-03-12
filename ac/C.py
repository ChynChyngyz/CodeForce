def main():
    n, q = map(int, input().split())
    for _ in range(n):
        l, r = list(map(int, input().split()))
    for _ in range(q):
        t = int(input())

    def solve(n, q, l, r, t):
        out = 0
        for i, j in enumerate(range(l, r)):
            print(f"Индекс {j}: {i}")
            print(f"Первый элемент {j}: {i[0]}")
            print(f"Второй элемент {j}: {i[1]}")
        return out

if __name__ == '__main__':
    main()

