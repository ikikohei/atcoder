def main():
    from decimal import Decimal
    a, b, c, d = map(str, input().split())
    a, b, c, d = Decimal(a), Decimal(b), Decimal(c), Decimal(d)
    if b - c * d == 0:
        m = b*1 + a
        r = c * d * 1
        if m <= r:
            return print(1)
        else: return print(-1)
    x = -1 * a / (b-d*c)
    if x < 0:
        return print(-1)
    if x == int(x):
        return print(int(x))
    return print(int(x)+1)

if __name__=="__main__":
    main()