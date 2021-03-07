def coins(A,B,C):
    dp = [[[i for i in range(101)]for j in range(101)]for k in range(101)]
    for i in range(100,-1,-1):
        for j in range(100,-1,-1):
            for k in range(100,-1,-1):
                if i == 0 and j == 0 and k == 0:
                    dp[i][j][k] = 0
                    continue
                if i == 100 or j == 100 or k == 100:
                    dp[i][j][k] = 0
                    continue
                if i == 99 and j == 99 and k == 99:
                    dp[i][j][k] = 1
                    continue
                dp[i][j][k] = dp[i+1][j][k]*i/(i+j+k) + dp[i][j+1][k]*j/(i+j+k) + dp[i][j][k+1]*k/(i+j+k) + 1
    print(dp[A][B][C])

def main():
    A, B, C = map(int, input().split())
    coins(A,B,C)

if __name__=='__main__':
    main()
