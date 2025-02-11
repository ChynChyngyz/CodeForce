t = int(input())
for i in range(t):
    n = int(input())
    br = [False] * (n + 1)
    free_princess = -1
    for princess in range(1, n + 1):
        n_list = list(map(int, input().split()))
        k = n_list[0]
        pr = n_list[1:]
        boolean = False
        for p in pr:
            if not br[p]:
                br[p] = True
                boolean = True
                break
        if not boolean:
            free_princess = princess

    free_prince = -1
    for p in range(1, n + 1):
        if not br[p]:
            free_prince = p
            break

    if free_prince == -1:
        print("OPTIMAL")
    else:
        print(f"IMPROVE\n{free_princess} {free_prince}")
