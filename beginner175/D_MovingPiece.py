def main():
    n, k = map(int, input().split())
    # p = list(map(int, input().split()))
    p = [int(x) - 1 for x in input().split()]
    c = [int(x) for x in input().split()]
    f_inf = float('inf')
    ans = [-f_inf]
    for i in range(n):
        pnt_list = [0]
        nxt = i
        for j in range(min(k,n)):
            pnt_list.append(pnt_list[-1] + c[p[nxt]])
            nxt = p[nxt]
            if nxt == i:
                if pnt_list[-1] > 0:
                    tmp1 = pnt_list[-1] * (k//(j+1)) + max(pnt_list[:k%(j+1)+1])
                    tmp2 = pnt_list[-1] * (k//(j+1) - 1) + max(pnt_list[1:])
                    tmp = max(tmp1,tmp2)
                else: tmp = max(pnt_list[1:])
                pnt_list.append(tmp)
                break
        ans.append(max(pnt_list[1:]))
    print(max(ans))

if __name__=='__main__':
    main()