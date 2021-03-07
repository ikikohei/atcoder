def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    mapping = {}
    for i, a in enumerate(a_list):
        if a not in mapping:
            mapping[a] = []
        mapping[a].append(i+1)
    print(mapping)
    for i in range(n+1):
        pre = 0
        if i not in mapping:
            return print(i)
        for index in mapping[i]:
            if index - pre > m:
                return print(i)
            pre = index
        if n+1 - pre > m:
            return print(i)

if __name__=='__main__':
    main()


