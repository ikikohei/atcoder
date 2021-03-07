# LCS(最長共通文字列)アルゴリズムを使ったパターン
# これだとこの問題は解けないが LCS の基本はこれ
def main():
    N, M = map(int, input().split())
    A = [ax for ax in map(int,input().split())]
    B = [bx for bx in map(int,input().split())]
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for ni in range(1,N+1):
        for mi in range(1,M+1):
            if A[ni-1] == B[mi-1]:
                dp[ni][mi]=dp[ni-1][mi-1]+1
            else:
                dp[ni][mi]=max(dp[ni-1][mi], dp[ni][mi-1])
    print(dp)
    lcs = dp[N][M]
    cost = abs(N-M) + (min(N,M) - lcs)
    print(cost)

if __name__ == "__main__":
    main()