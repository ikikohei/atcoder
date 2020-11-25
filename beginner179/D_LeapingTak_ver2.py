# dp 法 + 累積和をもちいて計算時間を短縮したい
def leapingTak(N, sections):
    const = 998244353
    # print(sections)
    dp = [0 for i in range(N+1)]
    dp[1] = 1
    s = 0
    e = 0
    for j in range(2,N+1):
        dp[j] = dp[j-1]
        for section in sections:
            s = section[0]
            e = section[1]
            if s > j:
                continue
            if e+1 > j:
                dp[j] += dp[j-s] - dp[0]
                continue
            dp[j] += dp[j-s] - dp[j-e-1]
        dp[j] = dp[j] % const
    # print(dp)
    return dp[N] - dp[N-1] if (dp[N]-dp[N-1]) >= 0 else const + dp[N] - dp[N-1]
    # return dp[N]-dp[N-1]


def main():
    N,K = map(int,input().split())
    sections = []
    for i in range(K):
        section = list(map(int,input().split()))
        sections.append(section)
    print(leapingTak(N,sections))
    
if __name__=='__main__':
    main()

