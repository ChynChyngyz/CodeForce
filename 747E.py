# def main():
#     a = []
#     s = input().split(',')
#     for i in range(0, len(s), 2):
#         a.append([s[i], s[i+1]])
#     k = 0
#     n = 0
#     for j, a in enumerate(a):
#         while k < len(a):
#             n+=1
#             if a[1] > 0:
#                 while j == a[1]:
#                     continue
#             elif
#             k+=1
#
#
# if __name__ == '__main__':
#     main()

a = []
s = input().split(',')
for i in range(0, len(s), 2):
    a.append([s[i], s[i+1]])
print(a)
for j, a in enumerate(a):
    print(f"Индекс {j}: {a}")
    print(f"Первый элемент {j}: {a[0]}")
    print(f"Второй элемент {j}: {a[1]}")
    print()