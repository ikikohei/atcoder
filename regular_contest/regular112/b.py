def main():
    from decimal import Decimal
    t = int(input())
    cases = []
    for i in range(t):
        cases.append(list(map(int,input().split())))
    for case in cases:
        num = case[1] - 2 * Decimal(str(case[0]))
        if num < 0: print(0)
        else:
            print(int(Decimal("0.5") * Decimal(str(num+1)) * Decimal(str(num+2))))

if __name__ == "__main__":
    main()

