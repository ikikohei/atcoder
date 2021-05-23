def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    import collections
    a_dict = collections.defaultdict(int)
    c_dict = collections.defaultdict(int)
    for (_a, _c) in zip(a, c):
        a_dict[_a] += 1
        c_dict[b[_c-1]] += 1
    count = 0
    for k, v in a_dict.items():
        if k in c_dict:
            count += v * c_dict[k]
    print(count)

if __name__=="__main__":
    main()



        