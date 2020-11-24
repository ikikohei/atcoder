def DPmethodforFrogProbrem(N,h):
    # dp[i] に行くのは dp[i-1] から1段分のコストを払っていくか
    # dp[i-2] から2段分のコストを払っていくか
    # 配列にしてどっちかコストの低い方で埋めていけばいい
    dp = [0] * (N+10) 
    dp[1] = abs(h[1] - h[0])
    for i in range(N-2):
        if dp[i]+abs(h[i+2]-h[i]) < dp[i+1] + abs(h[i+2]-h[i+1]):
            dp[i+2] = dp[i] + abs(h[i+2] - h[i])
        else:
            dp[i+2] = dp[i+1] + abs(h[i+2] - h[i+1])
    return dp

def main():
    N = int(input())
    hight = list(map(int,input().split()))
    dp = DPmethodforFrogProbrem(N,hight)
    # print(dp)
    print(dp[N-1])

if __name__=='__main__':
    main()

