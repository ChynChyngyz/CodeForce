def main():
    n_k=input().split()
    n = int(n_k[0])
    k = int(n_k[1])

    b_r = list(map(int, input().split()))
    w_r = list(map(int, input().split()))
    val =list(map(int, input().split()))

    if 1 >=k:
        print(0)
        return

    diff = [0] * (k+2)
    for i in range(n):
        L = b_r[i]
        R = k-w_r[i]
        if L > R:
            continue
        if L < 1:
            L=1
        if R>k-1:
            R=k-1
        if R >= L:
            diff[L] +=val[i]
            diff[R+1] -=val[i]

    max_val =0
    curr=0
    for j in range(1, k):
        curr += diff[j]
        if curr > max_val:
            max_val = curr
    print(max_val)

if __name__ == '__main__':
    main()