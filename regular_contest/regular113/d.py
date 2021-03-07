def main():
    n, m, k = map(int, input().split())
    ans = 0
    split_num = 998244353
    for ki in range(k):
        ans += ((ki+1)**n - ki**n)*(k - ki)**m % split_num
        ans = ans % split_num
    print(ans)

if __name__=='__main__':
    main()
