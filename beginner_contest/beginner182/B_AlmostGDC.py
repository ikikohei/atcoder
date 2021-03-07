N = int(input())
numList = list(map(int, input().split(" ")))
GDCMax = 0
GDC=0

maxNum = max(numList)
for n in range(maxNum):
    k = n+2
    for i in range(0,N):
        if(numList[i] % k == 0):
            GDC += 1
    if(GDCMax<GDC):
        GDCMax=GDC
        ans=n
    GDC=0

# print(GDCMax)
print(ans)