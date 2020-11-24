def knapsack(N,W,items):
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for n in range(N):
        for w in range(W):
            if items[n][0] <= w+1:
                dp[n+1][w+1] = max(dp[n][w+1],dp[n][w+1-items[n][0]]+items[n][1])
            else:
                dp[n+1][w+1] = dp[n][w+1]
    return dp



def main():
    N, W = map(int, input().split())
    items = []
    for i in range(N):
        items.append(list(map(int, input().split())))
    print(items)
    dp = knapsack(N,W,items)
    print(dp)
    print(dp[N][W])

if __name__=='__main__':
    main()
