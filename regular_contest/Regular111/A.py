def main():
    from decimal import Decimal
    # n, m = input().split()
    n, m = map(int,input().split())
    # print((10**n//m)%m)
    print((Decimal("10")**Decimal(n)//Decimal(m))%Decimal(m))
    

if __name__ == "__main__":
    main()