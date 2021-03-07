def logs(n):
    # import math
    import decimal
    a = decimal.Decimal("-1")
    bb = decimal.Decimal("1")
    ac = decimal.Decimal("8")
    x = decimal.Decimal(n+1)
    h = decimal.Decimal("0.5")
    db = decimal.Decimal("2")
    # n+1 の長さの丸太で 1~ どこまでの長さの丸太をカバーできるか計算する（無理やり）
    splitNumCoveredMaxLog = int((a+(bb+ac*x)**(h))/db)
    return n - splitNumCoveredMaxLog + 1

def main():
    n = int(input())
    print(logs(n))
    
if __name__=='__main__':
    main()
