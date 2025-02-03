n, m, k = map(int, input().split())
roads = []
for i in range(m):
    u, v, l = map(int, input().split())
    roads.append((u, v, l))

if k == 0:
    print(-1)
    exit()

pamyat = set(map(int, input().split()))
min_d = float('inf')

for u, v, l in roads:
    if (u in pamyat and v not in pamyat) or (v in pamyat and u not in pamyat):
        min_d = min(min_d, l)

print(min_d if min_d != float('inf') else -1)