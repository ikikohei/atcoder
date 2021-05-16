def main():
    n = int(input())
    master = []
    for _ in range(n):
        master.append(list(map(int, input().split())))
    l = 0
    h = 1001001001
    while l+1 < h:
        m = (l + h) // 2
        s = set()
        for p in master:
            score = 0
            for i in reversed(range(5)):
                if p[i] >= m:
                    score += 2**i
            s.add(score)
        ok = False
        s = list(s)
        for i in range(len(s)):
            for j in range(len(s)):
                for k in range(len(s)):
                    if s[i] | s[j] | s[k] == 31:
                        ok = True
        if ok: l = m
        else: h = m
    print(l)

if __name__=="__main__":
    main()

