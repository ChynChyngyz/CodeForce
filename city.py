import heapq


def main(n, m, roads, s, t):
    adj = [[] for _ in range(n+1)]
    for a, b, w in roads:
        adj[a].append((b, w))

    cap = [0] * (n+1)
    cap[s] = float('inf')

    heap = [(-cap[s], s)]

    while heap:
        curr_cap, u = heapq.heappop(heap)
        curr_cap = -curr_cap

        if u == t:
            return curr_cap

        if cap[u] > curr_cap:
            continue

        for v, w in adj[u]:
            new_cap = min(curr_cap, w)
            if cap[v] < new_cap:
                cap[v] = new_cap
                heapq.heappush(heap, (-cap[v], v))


n = int(input())
m = int(input())
s = int(input())
t = int(input())

roads = []
for i in range(m):
    a, b, w = map(int, input().split())
    roads.append((a, b, w))

res = main(n, m, roads, s, t)
print(f"Города {s} и {t}\n"
      f"Пропускная способность - {res}\n")

'''
4
4
1
4

[
    (1, 2, 30),
    (2, 3, 20),
    (3, 4, 10),
    (1, 4, 40)
]

= 40
'''




