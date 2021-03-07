def main():
    N = int(input())
    # lengthList = []
    ans = 0
    lengthList = list(map(int,input().split()))
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if lengthList[i] == lengthList[j] or lengthList[j] == lengthList[k] or lengthList[i] == lengthList[k]:
                    continue
                if lengthList[i] + lengthList[j] <= lengthList[k] or lengthList[j] + lengthList[k] <= lengthList[i] or lengthList[i] + lengthList[k] <= lengthList[j]:
                    continue
                ans += 1
    print(ans)

if __name__=='__main__':
    main()
        