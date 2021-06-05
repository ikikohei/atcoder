from collections import defaultdict

def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    after_rep = defaultdict(list)
    for i, m in enumerate(s):
        for j, c in enumerate(m):
            after_rep[i+j].append(c)
    ans = 1
    # print(after_rep)
    for l in after_rep.values():
        s = set(l)
        count = 0
        if "R" in s and "B" in s:
            return print(0)
        if "R" not in s and "B" not in s:
            count = 2
        else:
            count = 1
        ans *= count
    N = 998244353
    print(ans % N)

if __name__=="__main__":
    main()
        




    
