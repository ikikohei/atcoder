def main():
    from decimal import Decimal
    v, t, s, d = input().split()
    if Decimal(v)*Decimal(t) <= int(d) <= Decimal(v)*Decimal(s): return print("No")
    return print("Yes")
    
if __name__ == "__main__":
    main()