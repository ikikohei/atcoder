def main():
    import math
    from decimal import Decimal
    n = int(input())
    route_n = int(math.sqrt(Decimal(str(n))))
    # print(route_n)
    log_n = int(math.log(Decimal(str(n)),Decimal("2")))
    # print(log_n)
    s = set()
    ans = 0
    for i in range(2,route_n+2):
        # print(i)
        for j in range(2, log_n+2):
            if i**j not in s and i**j <= n:
                s.add(i**j)
                ans += 1
            if i ** j > n: break
        # print(j)
    print(n-ans)

if __name__=='__main__':
    main()

