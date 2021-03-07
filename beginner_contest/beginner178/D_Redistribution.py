def redistribution(S):
    if S <= 2: return 0
    const = 10**9 + 7
    dp = [0 for i in range(2001)]
    for j in range(3,2001):
        for k in range(j-2):
            dp[j] += dp[k]
        dp[j] = (dp[j] + 1)%const
        if j == S: break
    return dp[S]

def main():
    S = int(input())
    print(redistribution(S))

if __name__=='__main__':
    main()