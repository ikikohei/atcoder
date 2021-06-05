from collections import defaultdict

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    ruiseki = [0]
    for i, _a in enumerate(a):
        if i % 2 == 1:
            _a = -_a
        s += _a
        ruiseki.append(s)
    d = defaultdict(int)
    ans = 0
    for r in ruiseki:
        # print("r: {} , d[r]: {}".format(r, d[r]))
        if r in d:
            ans += d[r]
        d[r] += 1
    print(ans)

if __name__=="__main__":
    main()




        
