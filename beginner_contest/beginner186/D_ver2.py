def main():
    n = int(input())
    numlist = list(map(int,input().split()))
    numlist.sort()
    ans = 0
    # counter = 0
    ruisekiwa = 0
    for i in range(1,n):
        # counter = numlist[i]*i
        ruisekiwa += numlist[i-1]
        ans += numlist[i]*i - ruisekiwa
    print(ans)

if __name__ == "__main__":
    main()
