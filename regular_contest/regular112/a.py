def main():
    from decimal import Decimal
    b, c = map(int,input().split())
    ans = 0
    if b <= 0:
        ans += Decimal(str(c)) // 2
        ans += Decimal(str(c-1))//2
        ans += min(2*abs(b)+1, c)
    else:
        ans += Decimal(str(c-1))//2
        ans += Decimal(str(c-2))//2
        ans += min(abs(b*2+1), c+1)
    print(ans)


if __name__ == "__main__":
    main()