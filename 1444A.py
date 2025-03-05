# def main():
#     t = int(input())
#     for i in range(t):
#         q, p = map(int, input().split())
#         x = max(q, p)
#         j =0
#         while j<x:
#             if (p%x==0 and q%x!=0):
#                 x-=1
#                 print(x)
# if __name__ == '__main__':
#     main()

for ch in range(ord('a'), ord('z')+1):
    print(chr(ch))
