def main():
    n = int(input())
    t = list(map(int, input().split()))
    t = [0] + t
    s = sum(t)
    if s % 2 == 0: half = s//2
    else: half = s//2 + 1
    dp = [[False for _ in range(s+1)] for _ in range(n+1)]
    dp[0][0] = True
    # print(t)
    for i in range(1,n+1):
        for j in range(s + 1):
            if j == 0:
                dp[i][j] = True
            if t[i] > j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-t[i]] or dp[i-1][j]
    # print(dp)
    for k in range(half, s+1):
        if dp[n][k]:
            return print(k)

if __name__=="__main__":
    main()