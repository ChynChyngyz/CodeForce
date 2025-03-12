def main(n, k,q):
    tr=[input() for _ in range(n)]
    parent=list(range(n))
    size=[0]*n
    max=1

    def f(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a= parent[a]
        return a

    def u(a, b):
        nonlocal max
        a=f(a)
        b=f(b)
        parent[b] = a
        size[a] += size[b]
        if a==b:
            return
        if size[a]<size[b]:
            a, b = b, a
        if size[a]>max:
            max=size[a]
    process =[False]*k
    ans=[]

    for _ in range(q):
        parts =input().split()
        t =int(parts[0])
        if t==1:
            j=int(parts[1])-1
            if process[j]:
                continue
            process[j] = True
            groups={chr(c): [] for c in range(ord('a'), ord('z') + 1)}
            for i in range(n):
                groups[tr[i][j]].append(i)
            for letter in groups:
                l=groups[letter]
                if len(l)<2:
                    continue
                for i in range(1, len(l)):
                    u(l[i-1], l[i])

        elif t==2:
            i=int(parts[1])-1
            root=f(i)
            ans.append(str(size[root]))
        elif t==3:
            ans.append(str(max))

    print('\n'.join(ans))


if __name__ == '__main__':
    n, k, q=int(input()), int(input()), int(input())
    main(n,k,q)

# def main(n, k, q):
#     traits = [input().strip() for _ in range(n)]
#     parent = list(range(n))
#     size = [1] * n
#     global_max = 1
#
#     def find(a):
#         while parent[a] != a:
#             parent[a] = parent[parent[a]]
#             a = parent[a]
#         return a
#
#     def union(a, b):
#         nonlocal global_max
#         a = find(a)
#         b = find(b)
#         if a == b:
#             return
#         if size[a] < size[b]:
#             a, b = b, a
#         parent[b] = a
#         size[a] += size[b]
#         if size[a] > global_max:
#             global_max = size[a]
#     processed = [False] * k
#     answers = []
#
#     for _ in range(q):
#         parts = input().split()
#         t = int(parts[0])
#         if t == 1:
#             j = int(parts[1]) - 1
#             if processed[j]:
#                 continue
#             processed[j] = True
#             groups = {chr(c): [] for c in range(ord('a'), ord('j') + 1)}
#             for i in range(n):
#                 groups[traits[i][j]].append(i)
#             for letter in groups:
#                 lst = groups[letter]
#                 if len(lst) < 2:
#                     continue
#                 for i in range(1, len(lst)):
#                     union(lst[i - 1], lst[i])
#
#         elif t == 2:
#             i = int(parts[1]) - 1
#             root = find(i)
#             answers.append(str(size[root]))
#         elif t == 3:
#             answers.append(str(global_max))
#
#     print("\n".join(answers))
#
#
# if __name__ == '__main__':
#     n, k, q = map(int, input().split())
#     main(n, k, q)
