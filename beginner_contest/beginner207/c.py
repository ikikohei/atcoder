def minmax(t, l, r):
    s = 10**-3
    if t == 1:
        return l, r
    if t == 2:
        return l, r-s
    if t == 3:
        return l+s, r
    if t == 4:
        return l+s, r-s

def main():
    n = int(input())
    kukan = []
    for _ in range(n):
        t, l, r = map(int, input().split())
        kukan.append([t,l,r])
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            l1, r1 = minmax(kukan[i][0], kukan[i][1], kukan[i][2])
            l2, r2 = minmax(kukan[j][0], kukan[j][1], kukan[j][2])
            # print(l1, r1, l2, r2)
            if r2 < l1 or r1 < l2:
                continue
            ans += 1
    print(ans)

if __name__=="__main__":
    main()
