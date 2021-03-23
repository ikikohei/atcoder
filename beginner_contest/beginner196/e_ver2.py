def main():
    n = int(input())
    INF = 10 ** 19 - 1
    s = 0
    upper = INF
    under = - INF
    for _ in range(n):
        a, t = map(int, input().split())
        if t == 1:
            s += a
            upper += a
            under += a
        if t == 2:
            under = max(under, a)
            upper = max(upper, a)
        if t == 3:
            upper = min(upper, a)
            under = min(under, a)
    # print(under)
    # print(upper)
    q = int(input())
    x_list = list(map(int, input().split()))
    for x in x_list:
        if x + s <= under:
            print(under)
        elif x + s>= upper:
            print(upper)
        else:
            print(x+s)

if __name__=='__main__':
    main()