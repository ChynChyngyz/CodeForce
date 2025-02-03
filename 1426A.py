import math
n = int(input())
flat = []

for i in range(n):
    a, b = map(int, input().split())
    if a <= 2:
        flat.append(1)
    else:
        t = math.ceil(((a - 2)/b)+1)
        flat.append(t)

for i in flat:
    print(i)

# 4
# 7 3
# 1 5
# 22 5
# 987 13

# 3
# 1 
# 5
# 77
