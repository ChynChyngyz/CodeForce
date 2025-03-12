def main(n, n_i):
    sort_n_i=sorted(n_i)
    position={value: x for x, value in enumerate(sort_n_i)}
    perestanovka=[position[j] for j in n_i]
    visited=[False]*n
    c=0

    for i in range(n):
        if not visited[i]:
            c+=1
            k=i
            while not visited[k]:
                visited[k]=True
                k=perestanovka[k]
    if (n-c)%2==0:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    n=int(input())
    n_i = list(map(int, input().split()))
    main(n, n_i)