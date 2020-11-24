def DPmethodForFrog2(N,h,K):
    max_val = 10000000000
    dp = [max_val]*(10**5 + 1)
    dp[0] = 0
    for i in range(N-1):
        # if i+1 <= K:
        #     for j in range(i+1):
        #         if dp[i+1] > dp[j]+abs(h[i+1] - h[j]):
        #             dp[i+1] = dp[j] + abs(h[i+1]-h[j])
        # else:
        t = min(i+1,K)
        for l in range(i+1-t,i+1):
            if dp[i+1] > dp[l] + abs(h[i+1] - h[l]):
                dp[i+1] = dp[l] + abs(h[i+1]-h[l])
    return dp
    

def main():
    N, K = map(int,input().split())
    hight = list(map(int,input().split()))
    dp = DPmethodForFrog2(N,hight,K)
    print(dp[N-1])

if __name__=='__main__':
    main()
