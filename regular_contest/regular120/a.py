def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = 0
    s = 0
    rouriwa = []
    for _a in a:
        s += _a
        rouriwa.append(s)
    ruiseki_ruiseki = []
    s = 0
    for _b in rouriwa:
        s += _b
        ruiseki_ruiseki.append(s)
    for i in range(n):
        m = max(m, a[i]) 
        ans = 0
        if i > 0:
            ans += ruiseki_ruiseki[i-1]
        ans += m * (i+1)
        ans += rouriwa[i]
        print(ans)
    
if __name__=="__main__":
    main()


