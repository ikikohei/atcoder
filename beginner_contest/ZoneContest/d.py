def main():
    from collections import deque
    s = input()
    t = deque()
    rev = False
    for c in s:
        if c == "R":
            rev = not rev
            continue
        if rev:
            t.appendleft(c)
        else:
            t.append(c)
    ans = []
    if rev:
        t = reversed(t)
    for i in t:
        if len(ans) != 0 and ans[-1] == i:
            ans.pop()
            continue
        ans.append(i)
    print("".join(ans))

if __name__=="__main__":
    main()
