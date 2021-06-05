def main():
    n = int(input())
    s = input()
    t = input()
    zero_list_a = []
    zero_list_b = []
    for i, (_s, _t) in enumerate(zip(s, t)):
        if _s == "0":
            zero_list_a.append(i)
        if _t == "0":
            zero_list_b.append(i)
    if len(zero_list_a) != len(zero_list_b):
        return print(-1)
    ans = 0
    for (a, b) in zip(zero_list_a, zero_list_b):
        if a != b:
            ans += 1
    print(ans)

if __name__=="__main__":
    main()
