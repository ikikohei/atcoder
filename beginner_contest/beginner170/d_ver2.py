def main():
    from collections import defaultdict
    n = int(input())
    a_list = list(map(int, input().split()))
    a_dict = defaultdict(int)
    for a in a_list:
        i = a
        if a_dict[a] >= 1:
            a_dict[a] += 1
            continue
        while i <= 10**6+7:
            a_dict[i] += 1
            i += a
    ans = 0
    for a in a_list:
        # print("num {}, a {}".format(a_dict[a],a))
        if a_dict[a] == 1:
            ans += 1
    print(ans)

if __name__=="__main__":
    main()
    
        