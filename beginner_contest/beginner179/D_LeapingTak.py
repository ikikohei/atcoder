# シンプルにdp 法を使う
# これだと長い奴は間に合わなくなる
def leapingTak(N, sections):
    dp = [0 for i in range(N+1)]
    dp[1] = 1
    for j in range(1,N+1):
        for section in sections:
            if j + section > N:
                continue
            dp[j+section] += dp[j]
    # print(dp)
    return dp[N]


def main():
    N,K = map(int,input().split())
    sections = []
    for i in range(K):
        L,R = map(int,input().split())
        for j in range(L,R+1):
            sections.append(j)
    print(leapingTak(N,sections))
    
if __name__=='__main__':
    main()

