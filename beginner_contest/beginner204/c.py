def main():
    from collections import defaultdict
    n, m = map(int, input().split())
    dic = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        dic[a].append(b)
    ans = 0
    for i in range(n):
        tmp = set(dic[i+1])
        tmp_list = list(tmp)
        tmp.add(i+1)
        for j in tmp_list:
            for k in dic[j]:
                if k not in tmp:
                    tmp.add(k)
                    tmp_list.append(k)
        ans += len(tmp)
    print(ans)

if __name__=="__main__":
    main()

        

        

