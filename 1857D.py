def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        c = [a[i] - b[i] for i in range(n)]

        max_c = max(c)
        wise = [i +1 for i in range(n) if c[i] == max_c]

        print(len(wise))
        print(" ".join(map(str, wise)))

if __name__ == '__main__':
    main()