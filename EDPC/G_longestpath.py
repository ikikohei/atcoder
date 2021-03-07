def f(x,flag,dp,opponent_list):
    if flag[x]==1: return dp[x]
    flag[x] = 1
    fans = 0
    for y in opponent_list[x]:
        fans = max(fans, f(y,flag,dp,opponent_list)+1)
    dp[x] = fans
    return fans

def main():
    n, m = map(int,input().split())
    opponent_list = [[] for _ in range(n+1)]
    flag = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    for i in range(m):
        x, y = map(int,input().split())
        opponent_list[x-1].append(y-1)
    ans = 0
    for i in range(n+1):
        ans = max(ans,f(i,flag,dp,opponent_list))
    print(ans)

if __name__ == "__main__":
    main()

    
