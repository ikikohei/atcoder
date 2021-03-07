def main():
    n = int(input())
    INFTY = 10**9 + 1
    ans = INFTY
    for i in range(n):
        a, p, x = map(int, input().split())
        if a < x:
            ans = min(p, ans)
    if ans >= INFTY: return print(-1)
    print(ans)

if __name__=='__main__':
    main()