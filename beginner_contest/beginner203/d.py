def main():
    maxA = 10**9 + 1
    n, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    s = [[0 for _ in range(n+1)] for _ in range(n+1)]
    r = maxA
    l = -1
    limit = (k*k) // 2 + 1
    while l+1 < r:
        mid = (r + l) // 2
        # s(i,j) には a(0,0) ~ a(i-1,j-1)のうち、mid より大きいものの数を入れる（便宜的に、s(0,0) ~ s(i,0), s(j,0) はぜんぶ0）
        for i in range(n):
            for j in range(n):
                s[i+1][j+1] = s[i+1][j] +s[i][j+1] - s[i][j]
                if a[i][j] > mid: s[i+1][j+1] += 1
        exist = False
        # k * k の区間のうち、mid より大きいものの数が中央値より上にあるか下にあるか調べる
        # 一つでも下にある区間があれば、より小さい値で調べなおす
        for i in range(n-k+1):
            for j in range(n-k+1):
                if (s[i+k][j+k] + s[i][j] - s[i][j+k] - s[i+k][j] < limit):
                    exist = True
        if exist:
            r = mid
        else:
            l = mid
    print(r)

if __name__=="__main__":
    main()


