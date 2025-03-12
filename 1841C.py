def main():
    b = int(input())
    for i in range(b):
        s = input()
        n = len(s)
        max_n = -float('inf')

        def get_v(c):
            return {'A': 1, 'B': 10, 'C': 100, 'D': 1000, 'E': 10000}[c]

        def value(s):
            v = 0
            char = 'A'
            for c in reversed(s):
                if c < char:
                    v -= get_v(c)
                else:
                    v += get_v(c)
                    char = c
            return v

        for i in range(n):
            o_char = s[i]
            for n_char in ['A', 'B', 'C', 'D', 'E']:
                if n_char == o_char:
                    continue
                new_s = s[:i] + n_char + s[i+1:]
                c_v = value(new_s)
                if max_n < c_v:
                    max_n = c_v

        print(max_n)

if __name__ == '__main__':
    main()



# def calculate(s):
#     a = b = c = d = e = False
#     total = 0
#
#     for i in range(len(s) - 1, -1, -1):
#         if s[i] == 'A':
#             a = True
#             total += -1 if (b or c or d or e) else 1
#         elif s[i] == 'B':
#             b = True
#             total += -10 if (c or d or e) else 10
#         elif s[i] == 'C':
#             c = True
#             total += -100 if (d or e) else 100
#         elif s[i] == 'D':
#             d = True
#             total += -1000 if e else 1000
#         elif s[i] == 'E':
#             e = True
#             total += 10000
#
#     return total
#
#
# def main():
#     t = int(input())
#
#     for _ in range(t):
#         s = list(input())
#         indices = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1}
#
#         for i, char in enumerate(s):
#             if indices[char] == -1:
#                 indices[char] = i
#
#         res = calculate(s)
#
#         for char, index in indices.items():
#             if index != -1:
#                 for replacement in 'ABCDE':
#                     if replacement != char:
#                         s[index] = replacement
#                         res = max(res, calculate(s))
#                 s[index] = char
#
#         indices = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1}
#
#         for i in range(len(s) - 1, -1, -1):
#             if indices[s[i]] == -1:
#                 indices[s[i]] = i
#
#         for char, index in indices.items():
#             if index != -1:
#                 for replacement in 'ABCDE':
#                     if replacement != char:
#                         s[index] = replacement
#                         res = max(res, calculate(s))
#                 s[index] = char
#
#         print(res)
#
#
# if __name__ == "__main__":
#     main()

