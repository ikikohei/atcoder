def stepSum(N, heightList):
    sumOfSteps = 0
    if N == 1: return 0
    for i in range(1,N):
        if heightList[i] < heightList[i-1]:
            sumOfSteps += heightList[i-1] - heightList[i]
            heightList[i] = heightList[i-1]
    return sumOfSteps

def main():
    N = int(input())
    heightList = list(map(int, input().split()))
    print(stepSum(N, heightList))

if __name__=='__main__':
    main()