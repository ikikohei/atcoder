def calculatePatternAxBplusC(N):
    ans = 0
    for i in range(N-1):
        A = i+1
        count = (N-1) // A
        ans += count
    return ans

def main():
    N = int(input())
    print(calculatePatternAxBplusC(N))

if __name__=='__main__':
    main()
