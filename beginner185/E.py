def main():
    inf = 1001001001
    N, M = map(int,input().split())
    A = [ax for ax in map(int,input().split())]
    B = [bx for bx in map(int,input().split())]
    costMap = [[inf for i in range(M+1)] for j in range(N+1)]
    costMap[0][0]=0
    for ni in range(N+1):
        for mi in range(M+1):
            if ni < N:
                costMap[ni+1][mi] = min(costMap[ni+1][mi],costMap[ni][mi]+1)
            if mi < M:
                costMap[ni][mi+1] = min(costMap[ni][mi+1],costMap[ni][mi]+1)
            if ni < N and mi < M:
                cost = 0 if A[ni] == B[mi] else 1
                # print(cost)
                costMap[ni+1][mi+1] = min(costMap[ni+1][mi+1],costMap[ni][mi]+cost)
    # print(costMap)
    print(costMap[N][M])
    
if __name__ == "__main__":
    main()

