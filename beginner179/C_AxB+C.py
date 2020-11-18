def sumOfYakusu(N):
    import math
    count = 0
    # √N まで試せば OK.
    # 無理数になる場合、切り捨てる（int で丸める）
    maxNum = int(math.sqrt(N))
    for i in range(maxNum):
        d = i+1
        if N%d==0:
            count += 2
        if d == N//d:
            count -= 1
    return count

def main():
    N = int(input())
    ans = 0
    for i in range(N-1):
        ans += sumOfYakusu(i+1)
    print(ans)

if __name__=='__main__':
    main()
