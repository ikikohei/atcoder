def main():
    from decimal import Decimal
    n, x = map(int, input().split())
    drinks =[]
    for i in range(n):
        drinks.append(list(input().split()))
    alcohole = 0
    ans = 0
    for j in range(n):
        alcohole += Decimal(drinks[j][0]) * Decimal(drinks[j][1]) / Decimal("100")
        ans += 1
        if alcohole > x: return print(ans)
    print(-1)

if __name__ == "__main__":
    main()

