import bisect


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2

    finches = []
    for _ in range(n):
        l = int(data[idx])
        h = int(data[idx + 1])
        finches.append((l, h))
        idx += 2

    jetstreams = []
    for _ in range(m):
        a = int(data[idx])
        w = int(data[idx + 1])
        jetstreams.append((a, w))
        idx += 2

    if m == 0:
        result = [str(l) for l, h in finches]
        print(' '.join(result))
        return

    jetstreams.sort()

    a_list = [js[0] for js in jetstreams]
    w_list = [js[1] for js in jetstreams]

    prefix_w = [0] * (m + 1)
    for i in range(m):
        prefix_w[i + 1] = prefix_w[i] + w_list[i]

    def calc(h):
        count = bisect.bisect_right(a_list, h)
        first_ge = bisect.bisect_left(a_list, h)
        sum_less = prefix_w[first_ge]
        sum_equal = prefix_w[count] - prefix_w[first_ge]
        return 2 * sum_less + sum_equal

    result = []
    for l, h in finches:
        displacement = calc(h)
        final_position = l + displacement
        result.append(str(final_position))

    print(' '.join(result))


if __name__ == "__main__":
    main()