# コンプガチャ理論 (https://manabitimes.jp/math/1053)
def main():
    from decimal import Decimal
    n = int(input())
    ans = 0
    for i in range(1,n):
        ans += Decimal(str(n)) / Decimal(str(n - i))
    print(ans)

if __name__=='__main__':
    main()
