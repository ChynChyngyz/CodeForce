# def main():
#     n, k = map(int, input().split())
#     b = list(map(int, input().split()))
#     a = []
#
#     bambook_l = 0
#     bob_metr = 0
#     for i in range(n):
#         bambook_l += b[i]
#         bs_diff = bambook_l - bob_metr
#         if bs_diff < k:
#             bob_metr += bs_diff
#         else:
#             bob_metr += k
#
#     diff = bambook_l - bob_metr
#     if diff %k != 0:
#         time = diff // k+n+1
#     else:
#         time = diff // k+n
#     return time
#
# print(main())
#

def main():
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    a = []

    for num in b:
        if num > k:
            a.append(k)
        else:
            a.append(num)

    sum_b = sum(b)
    sum_a = sum(a)

    result = (sum_b/sum_a) * n - 1
    print(int(result))

if __name__ == '__main__':
    main()

