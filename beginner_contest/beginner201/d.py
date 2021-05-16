def main():
    INF = 10**9
    h, w = map(int, input().split())
    mass = []
    for _ in range(h):
        mass.append(input())
    if h == 1 and w == 1:
        return print("Draw")
    dp = [[-1 * INF for j in range(w)] for i in range(h)]
    dp[h-1][w-1] = 0
    for i in reversed(range(h)):
        for j in reversed(range(w)):
            if j < w-1:
                dp[i][j] = -1 * dp[i][j+1]
                if mass[i][j+1] == "+":
                    dp[i][j] += 1
                if mass[i][j+1] == "-":
                    dp[i][j] -= 1
            if i < h-1:
                if mass[i+1][j] == "+":
                    dp[i][j] = max(dp[i][j], -1 * dp[i+1][j] + 1)
                if mass[i+1][j] == "-":
                    dp[i][j] = max(dp[i][j], -1 * dp[i+1][j] - 1)
    if dp[0][0] == 0:
        return print("Draw")
    if dp[0][0] < 0:
        return print("Aoki")
    if dp[0][0] > 0:
        return print("Takahashi")

if __name__=="__main__":
    main()
    
    
            
                    
                


