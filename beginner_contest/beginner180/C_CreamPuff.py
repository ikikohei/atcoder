def devideCreammPuffNum(N):
    import math
    # √N まで試せば OK.
    # 無理数になる場合、切り捨てる（int で丸める）
    maxNum = int(math.sqrt(N))
    ans = []
    for i in range(maxNum):
        d = i+1
        if N%d==0:
            ans.append(d)
            ans.append(N//d)
    ans = set(ans)
    return sorted(ans)

def main():
    N = int(input())
    ans = devideCreammPuffNum(N)
    for i in ans:
        print(i)

if __name__=='__main__':
    main()
